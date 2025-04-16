from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename
import gemini_utils
import storage

app = Flask(__name__)
app.config.from_object('config')

# Ensure data directories exist
os.makedirs('data/templates', exist_ok=True)
os.makedirs('data/drafts', exist_ok=True)
os.makedirs('data/diagrams', exist_ok=True)

@app.route('/')
def index():
    templates = storage.get_templates()
    drafts = storage.get_drafts()
    return render_template('index.html', templates=templates, drafts=drafts)

@app.route('/new-grant', methods=['GET', 'POST'])
def new_grant():
    if request.method == 'POST':
        template_id = request.form.get('template_id')
        draft_id = str(uuid.uuid4())
        
        # Create new draft from template
        template = storage.get_template(template_id)
        draft = {
            'id': draft_id,
            'title': f"New Draft - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            'template_id': template_id,
            'sections': template['sections'],
            'answers': {},
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'diagrams': []
        }
        
        storage.save_draft(draft)
        return redirect(url_for('editor', draft_id=draft_id))
    
    templates = storage.get_templates()
    return render_template('new_grant.html', templates=templates)

@app.route('/upload-custom', methods=['POST'])
def upload_custom():
    if 'custom_template' not in request.files:
        return redirect(url_for('new_grant'))
    
    file = request.files['custom_template']
    if file.filename == '':
        return redirect(url_for('new_grant'))
    
    filename = secure_filename(file.filename)
    file_path = os.path.join('data/uploads', filename)
    os.makedirs('data/uploads', exist_ok=True)
    file.save(file_path)
    
    # Process the uploaded template with Gemini
    content = file.read().decode('utf-8')
    sections = gemini_utils.extract_sections_from_custom(content)
    
    # Create a new template from the uploaded content
    template_id = str(uuid.uuid4())
    template = {
        'id': template_id,
        'name': f"Custom - {filename}",
        'description': "Custom uploaded template",
        'sections': sections,
        'created_at': datetime.now().isoformat()
    }
    
    storage.save_template(template)
    
    # Create a new draft from this template
    draft_id = str(uuid.uuid4())
    draft = {
        'id': draft_id,
        'title': f"Custom Draft - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        'template_id': template_id,
        'sections': sections,
        'answers': {},
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
        'diagrams': []
    }
    answers = gemini_utils.generate_answers(sections, content)
    draft['answers'] = answers
    storage.save_draft(draft)
    return redirect(url_for('editor', draft_id=draft_id))

@app.route('/editor/<draft_id>')
def editor(draft_id):
    draft = storage.get_draft(draft_id)
    if not draft:
        return redirect(url_for('index'))
    
    template = storage.get_template(draft['template_id'])
    return render_template('editor.html', draft=draft, template=template)

@app.route('/diagrams/<draft_id>')
def diagrams(draft_id):
    draft = storage.get_draft(draft_id)
    if not draft:
        return redirect(url_for('index'))
    
    return render_template('diagrams.html', draft=draft)

@app.route('/preview/<draft_id>')
def preview(draft_id):
    draft = storage.get_draft(draft_id)
    if not draft:
        return redirect(url_for('index'))
    
    # Generate content with Gemini if not already generated
    if 'generated_content' not in draft:
        template = storage.get_template(draft['template_id'])
        draft['generated_content'] = gemini_utils.generate_grant_content(draft, template)
        storage.save_draft(draft)
    
    return render_template('preview.html', draft=draft)

@app.route('/api/save-answers', methods=['POST'])
def save_answers():
    data = request.json
    draft_id = data.get('draft_id')
    answers = data.get('answers')
    
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    draft['answers'] = answers
    draft['updated_at'] = datetime.now().isoformat()
    storage.save_draft(draft)
    
    return jsonify({'success': True})

@app.route('/api/save-diagram', methods=['POST'])
def save_diagram():
    data = request.json
    draft_id = data.get('draft_id')
    diagram_data = data.get('diagram')
    diagram_id = data.get('diagram_id', str(uuid.uuid4()))
    
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    # Create or update diagram
    diagram = {
        'id': diagram_id,
        'title': diagram_data.get('title', 'Untitled Diagram'),
        'type': diagram_data.get('type', 'flowchart'),
        'content': diagram_data.get('content', ''),
        'created_at': datetime.now().isoformat()
    }
    
    # Update draft with diagram reference
    if 'diagrams' not in draft:
        draft['diagrams'] = []
    
    # Check if diagram already exists
    existing_diagram = next((d for d in draft['diagrams'] if d['id'] == diagram_id), None)
    if existing_diagram:
        draft['diagrams'].remove(existing_diagram)
    
    draft['diagrams'].append(diagram)
    draft['updated_at'] = datetime.now().isoformat()
    storage.save_draft(draft)
    
    return jsonify({'success': True, 'diagram_id': diagram_id})

@app.route('/api/generate-section', methods=['POST'])
def generate_section():
    data = request.json
    draft_id = data.get('draft_id')
    section_id = data.get('section_id')
    
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    template = storage.get_template(draft['template_id'])
    section = next((s for s in draft['sections'] if s['id'] == section_id), None)
    
    if not section:
        return jsonify({'success': False, 'error': 'Section not found'})
    
    # Generate content for this specific section
    content = gemini_utils.generate_section_content(section, draft['answers'])
    
    return jsonify({'success': True, 'content': content})

@app.route('/api/export/<draft_id>/<format>')
def export_draft(draft_id, format):
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    if format == 'pdf':
        # PDF export logic would go here
        # For now, we'll just return the HTML content
        return render_template('export_pdf.html', draft=draft)
    elif format == 'html':
        return render_template('export_html.html', draft=draft)
    else:
        return jsonify({'success': False, 'error': 'Unsupported format'})

if __name__ == '__main__':
    # Initialize with default templates if none exist
    if not os.path.exists('data/templates') or len(os.listdir('data/templates')) == 0:
        storage.initialize_default_templates()
    
    app.run(debug=True)

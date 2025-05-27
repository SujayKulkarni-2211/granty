from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file, session
import os
import json
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename
import gemini_utils
import storage
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import markdown
import tempfile
import time
import hashlib
import random


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config.get('SECRET_KEY', 'dev-secret-key')

# Mock Razorpay Client Class
class MockRazorpayClient:
    def __init__(self, auth):
        self.key_id = auth[0]
        self.key_secret = auth[1]
        self.order = MockOrderAPI()
        self.utility = MockUtilityAPI()

class MockOrderAPI:
    def create(self, data):
        """Mock order creation - simulates Razorpay order creation"""
        order_id = f"order_{uuid.uuid4().hex[:16]}"
        
        # Store order details in session for later verification
        if 'mock_orders' not in session:
            session['mock_orders'] = {}
        
        session['mock_orders'][order_id] = {
            'id': order_id,
            'amount': data['amount'],
            'currency': data['currency'],
            'receipt': data['receipt'],
            'notes': data.get('notes', {}),
            'status': 'created',
            'created_at': datetime.now().isoformat()
        }
        
        return {
            'id': order_id,
            'amount': data['amount'],
            'currency': data['currency'],
            'receipt': data['receipt'],
            'status': 'created'
        }

class MockUtilityAPI:
    def verify_payment_signature(self, data):
        """Mock payment verification - simulates Razorpay signature verification"""
        order_id = data.get('razorpay_order_id')
        payment_id = data.get('razorpay_payment_id')
        signature = data.get('razorpay_signature')
        
        # Check if order exists
        if 'mock_orders' not in session or order_id not in session['mock_orders']:
            raise MockSignatureVerificationError("Order not found")
        
        # Simple signature validation (mock)
        expected_signature = hashlib.sha256(f"{order_id}|{payment_id}".encode()).hexdigest()
        
        if signature != expected_signature:
            raise MockSignatureVerificationError("Invalid signature")
        
        # Mark order as paid
        session['mock_orders'][order_id]['status'] = 'paid'
        session['mock_orders'][order_id]['payment_id'] = payment_id
        
        return True

class MockSignatureVerificationError(Exception):
    pass

# Initialize Mock Razorpay client
razorpay_client = MockRazorpayClient(auth=(
    app.config.get('RAZORPAY_KEY_ID', 'mock_key_id'),
    app.config.get('RAZORPAY_KEY_SECRET', 'mock_key_secret')
))

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
            'diagrams': [],
            'generated_content': None
        }
        
        storage.save_draft(draft)
        return redirect(url_for('editor', draft_id=draft_id))
    
    templates = storage.get_templates()
    return render_template('new_grant.html', templates=templates)

import PyPDF2

def extract_text_from_pdf(file_path):
    """Extract text content from a PDF file"""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

@app.route('/upload-custom', methods=['POST'])
def upload_custom():
    print("Processing custom template upload...")
    
    if 'custom_template' not in request.files:
        print("No file in request")
        return redirect(url_for('new_grant'))
    
    file = request.files['custom_template']
    if file.filename == '':
        print("Empty filename")
        return redirect(url_for('new_grant'))
    
    filename = secure_filename(file.filename)
    file_path = os.path.join('data/uploads', filename)
    os.makedirs('data/uploads', exist_ok=True)
    
    try:
        # Save the file first
        file.save(file_path)
        print(f"File saved to: {file_path}")
        
        # Extract content based on file type
        content = ""
        if filename.lower().endswith('.pdf'):
            print("Processing PDF file...")
            content = extract_text_from_pdf(file_path)
        else:
            # For text files
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
        print(f"Extracted content length: {len(content)} characters")
        
        if not content.strip():
            print("Warning: No content extracted from file")
            return jsonify({'error': 'Could not extract content from file'}), 400
        
        # Process the uploaded template with Gemini
        print("Processing with Gemini...")
        sections_with_sample_answers = gemini_utils.extract_sections_with_sample_answers(content)
        print(f"Gemini extracted {len(sections_with_sample_answers)} sections with sample answers")
        
        # Create a new template from the uploaded content
        template_id = str(uuid.uuid4())
        template = {
            'id': template_id,
            'name': f"Custom - {filename}",
            'description': "Custom uploaded template with AI-generated sample answers",
            'sections': sections_with_sample_answers,
            'created_at': datetime.now().isoformat()
        }
        
        storage.save_template(template)
        print(f"Template saved with ID: {template_id}")
        
        # Create a new draft from this template with pre-filled sample answers
        draft_id = str(uuid.uuid4())
        
        # Pre-fill answers with sample answers
        sample_answers = {}
        for section in sections_with_sample_answers:
            for question in section.get('questions', []):
                sample_answers[question['id']] = question.get('sample_answer', '')
        
        draft = {
            'id': draft_id,
            'title': f"Custom Draft - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            'template_id': template_id,
            'sections': sections_with_sample_answers,
            'answers': sample_answers,  # Pre-filled with sample answers
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'diagrams': [],
            'generated_content': None
        }
        
        storage.save_draft(draft)
        print(f"Draft created with ID: {draft_id} and pre-filled sample answers")
        return redirect(url_for('editor', draft_id=draft_id))
        
    except Exception as e:
        print(f"Error processing custom template: {e}")
        import traceback
        traceback.print_exc()
        return f"Error processing template: {e}", 500

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
    
    return render_template('preview.html', draft=draft)

@app.route('/api/save-answers', methods=['POST'])
def save_answers():
    try:
        data = request.json
        print(f"Received save request: {data}")
        
        draft_id = data.get('draft_id')
        answers = data.get('answers', {})
        
        if not draft_id:
            return jsonify({'success': False, 'error': 'Draft ID is required'})
        
        draft = storage.get_draft(draft_id)
        if not draft:
            return jsonify({'success': False, 'error': 'Draft not found'})
        
        # Update answers - merge with existing answers
        if 'answers' not in draft:
            draft['answers'] = {}
        
        draft['answers'].update(answers)
        draft['updated_at'] = datetime.now().isoformat()
        
        # Clear generated content so it gets regenerated with new answers
        draft['generated_content'] = None
        
        storage.save_draft(draft)
        print(f"Saved answers for draft {draft_id}: {len(answers)} answers")
        
        return jsonify({'success': True, 'message': f'Saved {len(answers)} answers'})
        
    except Exception as e:
        print(f"Error saving answers: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    data = request.json
    draft_id = data.get('draft_id')
    
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    template = storage.get_template(draft['template_id'])
    if not template:
        return jsonify({'success': False, 'error': 'Template not found'})
    
    try:
        # Generate content using Gemini
        content = gemini_utils.generate_grant_content(draft, template)
        
        # Save generated content
        draft['generated_content'] = content
        draft['updated_at'] = datetime.now().isoformat()
        storage.save_draft(draft)
        
        return jsonify({'success': True, 'content': content})
        
    except Exception as e:
        print(f"Error generating content: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/save-content', methods=['POST'])
def save_content():
    try:
        data = request.json
        draft_id = data.get('draft_id')
        content = data.get('content')
        
        if not draft_id or not content:
            return jsonify({'success': False, 'error': 'Missing draft ID or content'})
        
        draft = storage.get_draft(draft_id)
        if not draft:
            return jsonify({'success': False, 'error': 'Draft not found'})
        
        # Save the edited content
        draft['generated_content'] = content
        draft['updated_at'] = datetime.now().isoformat()
        storage.save_draft(draft)
        
        return jsonify({'success': True, 'message': 'Content saved successfully'})
        
    except Exception as e:
        print(f"Error saving content: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/create-payment-order', methods=['POST'])
def create_payment_order():
    try:
        data = request.json
        draft_id = data.get('draft_id')
        coupon_code = data.get('coupon_code', '').strip()
        
        # Check coupon code
        if coupon_code.lower() == 'grantyadmin':
            return jsonify({
                'success': True,
                'free_download': True,
                'message': 'Free download activated with admin coupon'
            })
        
        # Create Mock Payment order for paid download
        amount = 500  # 5 INR in paise
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': f'draft_{draft_id}_{uuid.uuid4().hex[:8]}',
            'notes': {
                'draft_id': draft_id,
                'download_type': 'pdf'
            }
        }
        
        order = razorpay_client.order.create(data=order_data)
        
        return jsonify({
            'success': True,
            'order_id': order['id'],
            'amount': amount,
            'currency': 'INR',
            'key': app.config.get('RAZORPAY_KEY_ID', 'mock_key_id')
        })
        
    except Exception as e:
        print(f"Error creating payment order: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/verify-payment', methods=['POST'])
def verify_payment():
    try:
        data = request.json
        
        # Verify payment signature using mock system
        razorpay_client.utility.verify_payment_signature({
            'razorpay_order_id': data['razorpay_order_id'],
            'razorpay_payment_id': data['razorpay_payment_id'],
            'razorpay_signature': data['razorpay_signature']
        })
        
        # Payment verified successfully
        session['payment_verified'] = True
        session['draft_id'] = data.get('draft_id')
        
        return jsonify({'success': True, 'verified': True})
        
    except MockSignatureVerificationError:
        return jsonify({'success': False, 'error': 'Payment verification failed'})
    except Exception as e:
        print(f"Error verifying payment: {e}")
        return jsonify({'success': False, 'error': str(e)})

def generate_pdf_from_html(html_content, title):
    """Generate PDF from HTML content"""
    try:
        # Create temporary file for PDF
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        
        # Convert markdown to HTML if needed
        if html_content.startswith('#') or '**' in html_content:
            html_content = markdown.markdown(html_content)
        
        # Create PDF document
        doc = SimpleDocTemplate(temp_file.name, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Add title
        title_style = styles['Title']
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 12))
        
        # Convert HTML to paragraphs (basic conversion)
        import re
        
        # Remove HTML tags and convert to paragraphs
        clean_text = re.sub('<[^<]+?>', '', html_content)
        paragraphs = clean_text.split('\n\n')
        
        for para in paragraphs:
            if para.strip():
                story.append(Paragraph(para.strip(), styles['Normal']))
                story.append(Spacer(1, 12))
        
        # Build PDF
        doc.build(story)
        
        return temp_file.name
        
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None

@app.route('/api/download-pdf/<draft_id>')
def download_pdf(draft_id):
    try:
        # Check if payment is verified or if it's a free download
        coupon_used = request.args.get('coupon') == 'grantyadmin'
        payment_verified = session.get('payment_verified', False) and session.get('draft_id') == draft_id
        
        if not (coupon_used or payment_verified):
            return jsonify({'success': False, 'error': 'Payment required'}), 403
        
        # Get draft
        draft = storage.get_draft(draft_id)
        if not draft:
            return jsonify({'success': False, 'error': 'Draft not found'}), 404
        
        # Generate PDF
        content = draft.get('generated_content', '')
        if not content:
            return jsonify({'success': False, 'error': 'No content to download'}), 400
        
        pdf_path = generate_pdf_from_html(content, draft['title'])
        if not pdf_path:
            return jsonify({'success': False, 'error': 'Failed to generate PDF'}), 500
        
        # Clear payment verification
        if not coupon_used:
            session.pop('payment_verified', None)
            session.pop('draft_id', None)
        
        # Send file
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name=f"{draft['title']}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"Error downloading PDF: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/export/<draft_id>/<format>')
def export_draft(draft_id, format):
    draft = storage.get_draft(draft_id)
    if not draft:
        return jsonify({'success': False, 'error': 'Draft not found'})
    
    if format == 'html':
        return render_template('export_html.html', draft=draft)
    else:
        return jsonify({'success': False, 'error': 'Unsupported format'})

@app.route('/opportunities', methods=['GET', 'POST'])
def opportunities():
    if request.method == 'GET':
        return render_template('opportunities.html')
    elif request.method == 'POST':
        content = ""
        # Check if a file was uploaded
        if 'opportunity_file' in request.files and request.files['opportunity_file'].filename != '':
            file = request.files['opportunity_file']
            if file.filename == '':
                print("Empty filename")
                return redirect(url_for('opportunities'))
            filename = secure_filename(file.filename)
            file_path = os.path.join('data/uploads', filename)
            os.makedirs('data/uploads', exist_ok=True)
            file.save(file_path)
            print(f"File saved to: {file_path}")

            if filename.lower().endswith('.pdf'):
                print("Processing PDF file...")
                content = extract_text_from_pdf(file_path)
            else:
                # For text files
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            print(f"Extracted content length: {len(content)} characters")
            
        # check if there is content
        if not content.strip():
            print("No content provided in file")
            content = request.form.get('research_text', '')
        if content.strip():
            # Process the content with Gemini
            result = gemini_utils.get_opportunities(content)
            return render_template('opportunities.html', opportunities=result)
        # If neither, just reload page
        return render_template('opportunities.html')
    
@app.route('/payment/<draft_id>')
def payment_page(draft_id):
    """Display payment page with QR code"""
    draft = storage.get_draft(draft_id)
    if not draft:
        return redirect(url_for('index'))
    
    # Generate unique payment ID for tracking
    payment_id = f"PAY_{int(time.time())}_{random.randint(1000, 9999)}"
    
    # Store payment session
    session['payment_id'] = payment_id
    session['draft_id_for_payment'] = draft_id
    session['payment_amount'] = 5  # ₹5
    session['payment_status'] = 'pending'
    
    return render_template('payment.html', 
                         draft=draft, 
                         payment_id=payment_id,
                         amount=5)

@app.route('/verify-payment-new', methods=['POST'])
def verify_payment_new():
    """Simulate payment verification"""
    try:
        data = request.json
        transaction_id = data.get('transaction_id', '').strip()
        payment_id = session.get('payment_id')
        draft_id = session.get('draft_id_for_payment')
        
        if not transaction_id:
            return jsonify({
                'success': False, 
                'message': 'Please enter transaction ID'
            })
        
        if not payment_id or not draft_id:
            return jsonify({
                'success': False, 
                'message': 'Payment session expired. Please try again.'
            })
        
        # Simple validation - check if transaction ID looks valid
        if len(transaction_id) < 8:
            return jsonify({
                'success': False, 
                'message': 'Invalid transaction ID. Please check and try again.'
            })
        
        # For demo purposes, accept any transaction ID that's longer than 8 characters
        # In real scenario, you'd verify with your payment processor
        
        # Mark payment as successful
        session['payment_status'] = 'completed'
        session['transaction_id'] = transaction_id
        
        return jsonify({
            'success': True, 
            'message': 'Payment verified successfully!',
            'transaction_id': transaction_id
        })
        
    except Exception as e:
        print(f"Payment verification error: {e}")
        return jsonify({
            'success': False, 
            'message': 'Payment verification failed. Please try again.'
        })

@app.route('/download-pdf-new/<draft_id>')
def download_pdf_new(draft_id):
    """Download PDF after payment verification"""
    try:
        # Check payment status
        if (session.get('payment_status') != 'completed' or 
            session.get('draft_id_for_payment') != draft_id):
            
            return redirect(url_for('payment_page', draft_id=draft_id))
        
        # Get draft
        draft = storage.get_draft(draft_id)
        if not draft:
            return jsonify({'error': 'Draft not found'}), 404
        
        # Check if content exists
        content = draft.get('generated_content', '')
        if not content:
            return jsonify({'error': 'No content to download. Please generate content first.'}), 400
        
        # Generate PDF
        pdf_path = generate_pdf_from_html(content, draft['title'])
        if not pdf_path:
            return jsonify({'error': 'Failed to generate PDF'}), 500
        
        # Clear payment session after successful download
        session.pop('payment_status', None)
        session.pop('payment_id', None)
        session.pop('draft_id_for_payment', None)
        session.pop('transaction_id', None)
        
        # Send file
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name=f"{draft['title']}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        print(f"PDF download error: {e}")
        return jsonify({'error': 'Download failed. Please try again.'}), 500

@app.route('/help')
def help_page():
    """Display help and support page"""
    return render_template('help.html')

if __name__ == '__main__':
    # Initialize with default templates if none exist
    if not os.path.exists('data/templates') or len(os.listdir('data/templates')) == 0:
        storage.initialize_default_templates()
    
    app.run(debug=True)
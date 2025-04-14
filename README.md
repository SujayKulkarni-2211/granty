# Grant Writing Assistant

A smart tool to help users generate professional grant proposals with AI assistance. This application uses Flask for the backend, simple JSON storage, and Gemini AI to generate and polish content.

## Features

- 📝 **Grant Generation** from predefined templates or custom formats
- 📋 **Rich Text Editor** with formatting interpretation
- 📊 **Diagram Creation** for visual support (flowcharts, mind maps, etc.)
- 🤖 **Gemini AI Integration** for content generation and improvement
- 📤 **Export to PDF** for submission-ready proposals

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. Clone the repository:
   ```
   git clone <repository-url>
   cd grant-writer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Create a `.env` file in the project root (or modify the existing one)
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your-gemini-api-key
     SECRET_KEY=a-secure-random-string
     ```

## Running the Application

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

- `app.py` - Main Flask application
- `config.py` - Configuration settings
- `storage.py` - Data storage functions (JSON-based)
- `gemini_utils.py` - Gemini API integration
- `static/` - Static assets (CSS, JavaScript, images)
- `templates/` - HTML templates
- `data/` - Data storage directory

## Usage Guide

### Creating a New Grant Draft

1. On the home page, select a template or upload your own format
2. Answer the template questions in the left sidebar
3. Click "Apply to Section" to generate content for each section
4. Use the rich text editor to make additional edits
5. Click "Generate Draft" to create a complete proposal

### Adding Diagrams/Figures

1. Click "Create Diagram" in the editor
2. Select a diagram type (flowchart, mind map, etc.)
3. Write the diagram code using Mermaid.js syntax
4. Save the diagram and insert it into your grant

### Polishing and Exporting

1. Use the "Polish Section" button to improve specific sections
2. Preview the complete grant in a print-friendly format
3. Export to PDF for submission

## Requirements

- Flask==2.3.3
- python-dotenv==1.0.0
- google-generativeai==0.3.0
- Werkzeug==2.3.7
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- itsdangerous==2.1.2

## License

This project is licensed under the MIT License - see the LICENSE file for details.
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Application settings
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'

# File paths
DATA_DIR = 'data'
TEMPLATES_DIR = os.path.join(DATA_DIR, 'templates')
DRAFTS_DIR = os.path.join(DATA_DIR, 'drafts')
DIAGRAMS_DIR = os.path.join(DATA_DIR, 'diagrams')
UPLOADS_DIR = os.path.join(DATA_DIR, 'uploads')

# Ensure directories exist
for directory in [DATA_DIR, TEMPLATES_DIR, DRAFTS_DIR, DIAGRAMS_DIR, UPLOADS_DIR]:
    os.makedirs(directory, exist_ok=True)

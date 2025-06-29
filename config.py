import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API key - Make sure this is set
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY not found in environment variables!")
    print("Please set your Gemini API key in the .env file")

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///granty.db')

# Razorpay credentials
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID', 'rzp_test_your_key_id')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET', 'your_key_secret')

# Application settings
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
DEBUG = os.getenv('FLASK_ENV', 'development') == 'development'

# User limits
MAX_PROJECTS_PER_USER = 5

# Email configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'your-email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your-app-password')

# Application URL for email links
APP_URL = os.getenv('APP_URL', 'http://localhost:5000')

# File paths
DATA_DIR = 'data'
TEMPLATES_DIR = os.path.join(DATA_DIR, 'templates')
DRAFTS_DIR = os.path.join(DATA_DIR, 'drafts')
DIAGRAMS_DIR = os.path.join(DATA_DIR, 'diagrams')
UPLOADS_DIR = os.path.join(DATA_DIR, 'uploads')

# Ensure directories exist
for directory in [DATA_DIR, TEMPLATES_DIR, DRAFTS_DIR, DIAGRAMS_DIR, UPLOADS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Validate critical environment variables
def validate_config():
    """Validate that critical configuration is present"""
    issues = []
    
    if not GEMINI_API_KEY:
        issues.append("GEMINI_API_KEY is required for AI functionality")
    
    if not EMAIL_ADDRESS or EMAIL_ADDRESS == 'your-email@gmail.com':
        issues.append("EMAIL_ADDRESS should be configured for email verification")
    
    if not EMAIL_PASSWORD or EMAIL_PASSWORD == 'your-app-password':
        issues.append("EMAIL_PASSWORD should be configured for email verification")
    
    if issues:
        print("Configuration Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease update your .env file with the correct values.")
        return False
    
    return True

# LangChain configuration
LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2', 'false').lower() == 'true'
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY', '')

# Web scraping configuration
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3

# AI Configuration
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 4000
AI_MODEL = 'gemini-2.5-flash'

print("Configuration loaded successfully!")
if DEBUG:
    print(f"Debug mode: {DEBUG}")
    print(f"Database URL: {DATABASE_URL}")
    print(f"Gemini API configured: {'Yes' if GEMINI_API_KEY else 'No'}")
    print(f"Email configured: {'Yes' if EMAIL_ADDRESS and EMAIL_ADDRESS != 'your-email@gmail.com' else 'No'}")
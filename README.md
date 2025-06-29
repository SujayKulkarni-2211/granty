# grantY - AI-Powered Document Creation Assistant

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A sophisticated AI-powered platform for creating professional documents including research grants, business proposals, pitch decks, executive summaries, and scientific proposals.

## 🚀 Features

### Document Types
- **Research Grants** (5 templates): NSF, NIH, DOE, ERC, SBIR
- **Pitch Decks** (5 templates): Tech Startup, SaaS, E-commerce, Biotech, Series A
- **Business Proposals** (5 templates): Corporate Partnership, Project, Service, Investment, Vendor
- **Executive Summaries** (5 templates): Business Plan, Project, Investment, Research, Strategic
- **Scientific Proposals** (5 templates): Academic Research, Clinical Trial, Laboratory, Field Study, Computational

### Core Features
- ✅ **25 Professional Templates** across 5 categories
- ✅ **AI-Powered Content Generation** using Google Gemini
- ✅ **Custom Template Upload** with AI analysis
- ✅ **Interactive Document Editor** with auto-save
- ✅ **Sidebar AI Chat Assistant** available on all pages
- ✅ **Document Export** (Word DOCX and PDF)
- ✅ **User Authentication** with email verification
- ✅ **Project Management** for logged-in users
- ✅ **Guest Mode** with limited features
- ✅ **Opportunity Discovery** (AI-powered funding search)
- ✅ **Responsive Design** with beautiful UI
- ✅ **Payment Integration** for document downloads

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.0** - Web framework
- **SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Google Gemini API** - AI content generation
- **python-docx** - Word document generation
- **ReportLab** - PDF generation
- **PyPDF2** - PDF text extraction

### Frontend
- **Bootstrap 5.3.0** - CSS framework
- **Font Awesome 6.4.0** - Icons
- **Vanilla JavaScript** - Interactive features
- **CSS3** with glassmorphism effects

### Database
- **SQLite** (development)
- **PostgreSQL** (production ready)

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/SujayKulkarni-2211/granty.git
cd granty
git checkout v1
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
# Required: Gemini AI API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Email Configuration (for user verification)
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# Optional: Database URL (defaults to SQLite)
DATABASE_URL=sqlite:///granty.db

# Optional: Security
SECRET_KEY=your_secret_key_here

# Optional: Application URL
APP_URL=http://localhost:5000
```

### 5. Get Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add it to your `.env` file

### 6. Initialize Database
```bash
python app.py
```
The database will be automatically created with sample templates on first run.

### 7. Run the Application
```bash
python app.py
```
Visit http://localhost:5000 in your browser.

## 📁 Project Structure
```
granty/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── storage.py            # Database operations
├── gemini_utils.py       # AI integration
├── email_utils.py        # Email functionality
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── data/                # Data directory
│   ├── templates/       # Template storage
│   ├── drafts/         # Draft storage (legacy)
│   └── uploads/        # File uploads
├── static/             # Static assets
│   └── images/         # Image files
└── templates/          # HTML templates
    ├── base.html       # Base template
    ├── index.html      # Homepage
    ├── dashboard.html  # User dashboard
    ├── new_document.html # Document creation
    ├── editor.html     # Document editor
    ├── preview.html    # Document preview
    ├── chat.html       # Chat interface
    ├── login.html      # User login
    ├── register.html   # User registration
    ├── opportunities.html # Funding opportunities
    ├── payment.html    # Payment page
    └── help.html       # Help & support
```

## 🎯 Usage Guide

### For Guests
1. Visit the homepage
2. Click "Create Document" in navigation
3. Choose from 25+ professional templates
4. Fill in the interactive form with AI assistance
5. Generate and preview your document
6. Download as Word or PDF (₹49 or use coupon "grantyadmin")

### For Registered Users
1. Create account and verify email
2. Access dashboard with project management
3. Create up to 5 projects simultaneously
4. Use AI chat assistant for guidance
5. Save and manage multiple documents
6. Access funding opportunity discovery

### AI Chat Assistant
- Available on all pages via floating chat button
- Provides context-aware assistance
- Helps with content improvement
- Offers writing suggestions
- Available for both guests and users

## 🔧 Configuration Options

### Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes | None |
| `EMAIL_ADDRESS` | SMTP email address | No | None |
| `EMAIL_PASSWORD` | SMTP app password | No | None |
| `DATABASE_URL` | Database connection string | No | SQLite |
| `SECRET_KEY` | Flask secret key | No | Auto-generated |
| `APP_URL` | Application base URL | No | localhost:5000 |

### Feature Toggles
Modify `config.py` to customize:
- `MAX_PROJECTS_PER_USER` - Project limit (default: 5)
- Email verification requirements
- Payment integration settings

## 🧪 Testing

### Manual Testing Checklist
- [ ] User registration and email verification
- [ ] Document creation across all 5 categories
- [ ] AI content generation functionality
- [ ] Custom template upload and processing
- [ ] Document editing and saving
- [ ] PDF/DOCX export functionality
- [ ] AI chat assistant responses
- [ ] Payment flow (with test transaction)
- [ ] Responsive design on mobile devices

### Known Issues (v1)
1. **AI Agent API Issues**: Complex agent system needs simplification
2. **Grant Opportunities**: Web scraping functionality requires enhancement
3. **Mobile Chat**: Sidebar chat needs mobile optimization
4. **Email Delivery**: SMTP configuration may require adjustment

## 🚀 Deployment

### Local Development
```bash
python app.py  # Runs on localhost:5000
```

### Production Deployment
1. Set environment variables
2. Configure production database (PostgreSQL recommended)
3. Set up email service (Gmail SMTP or SendGrid)
4. Configure reverse proxy (Nginx recommended)
5. Use WSGI server (Gunicorn recommended)

### Example Gunicorn Command
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker Support (Future)
Docker configuration will be added in future versions.

## 📚 API Documentation

### Chat API
```http
POST /api/chat
Content-Type: application/json

{
  "project_id": "uuid",
  "message": "User message"
}
```

### Content Generation API
```http
POST /api/generate-content
Content-Type: application/json

{
  "draft_id": "uuid"
}
```

### Document Download API
```http
GET /api/download-docx/{draft_id}?coupon=grantyadmin
GET /api/download-pdf/{draft_id}?coupon=grantyadmin
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Add comments for complex functions
- Test new features thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful content generation
- **Bootstrap** for responsive UI components
- **Font Awesome** for beautiful icons
- **Flask** community for excellent documentation

## 📞 Support

- **Email**: sujayvk.btech23@rvu.edu.in
- **GitHub Issues**: [Report bugs or request features](https://github.com/SujayKulkarni-2211/granty/issues)
- **Documentation**: Available in `/help` route of the application

## 🔮 Roadmap

### v1.1 (Next Release)
- [ ] Fix AI agent API stability
- [ ] Enhance grant opportunity discovery
- [ ] Improve mobile chat interface
- [ ] Add document collaboration features

### v2.0 (Future)
- [ ] Multi-language support
- [ ] Advanced AI features
- [ ] Team collaboration
- [ ] API for third-party integrations
- [ ] Docker containerization
- [ ] Advanced analytics

---

**Made with ❤️ by Sujay Kulkarni**

*Empowering researchers and professionals with AI-powered document creation*
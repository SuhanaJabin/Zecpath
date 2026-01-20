# Zecpath - AI-Powered Job Portal

An autonomous hiring platform that automates the entire recruitment process from resume screening to offer generation using AI.

## Project Structure

```
zecpath/
├── backend/
│   ├── data/                    # Resume files and datasets
│   ├── parsers/                 # Resume parsing utilities
│   ├── ats_engine/             # AI-powered ATS system
│   ├── screening_ai/           # AI voice screening service
│   ├── interview_ai/           # AI video interview service
│   ├── scoring/                # Candidate scoring algorithms
│   ├── utils/                  # Utility functions and helpers
│   │   ├── logger.py          # Logging configuration
│   │   └── config.py          # Application configuration
│   ├── tests/                  # Test scripts
│   │   ├── test_ats_engine.py
│   │   ├── test_screening_ai.py
│   │   └── test_interview_ai.py
│   ├── logs/                   # Application logs
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment variables template
│   └── venv/                  # Virtual environment
├── frontend/                   # React frontend application
├── ai-modules/                # Additional AI modules
└── README.md

```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd zecpath
```

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your actual credentials
```

### 3. Configure Environment Variables

Edit `backend/.env` and add your API keys:

```env
OPENAI_API_KEY=your_actual_key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
DATABASE_URL=your_database_url
```

### 4. Run Tests

```bash
# Run all tests
pytest backend/tests/ -v

# Run specific test file
pytest backend/tests/test_ats_engine.py -v

# Run with coverage
pytest backend/tests/ --cov=backend --cov-report=html
```

### 5. Start Development Server

```bash
cd backend
python app.py
```

## Module Descriptions

### ATS Engine (`ats_engine/`)
- Resume parsing and text extraction
- Skill identification and matching
- Candidate scoring and ranking
- Automated shortlisting

### Screening AI (`screening_ai/`)
- AI voice call automation
- Multilingual support
- Screening question generation
- Response analysis

### Interview AI (`interview_ai/`)
- Video interview management
- HR and technical interviews
- Behavioral monitoring
- Real-time scoring

### Scoring Module (`scoring/`)
- Multi-criteria evaluation
- Weighted scoring algorithms
- Decision automation
- Cross-round aggregation

## Testing

The project includes comprehensive test coverage:

- **Unit Tests**: Test individual components
- **Integration Tests**: Test module interactions
- **AI Tests**: Validate AI response quality

## Logging

All AI activities are logged in the `backend/logs/` directory:

- `ats_engine.log` - ATS operations
- `screening_ai.log` - Voice call activities
- `interview_ai.log` - Interview sessions
- `scoring.log` - Scoring calculations
- `api.log` - API requests

## Code Standards

- **Style Guide**: PEP 8
- **Formatter**: Black
- **Linter**: Flake8, Pylint
- **Documentation**: Google-style docstrings

```bash
# Format code
black backend/

# Lint code
flake8 backend/
pylint backend/
```

## Development Workflow

1. Create feature branch
2. Write code with tests
3. Run tests locally
4. Format and lint code
5. Commit with descriptive message
6. Push and create PR

## Technologies Used

- **Backend**: Python, FastAPI/Flask
- **AI**: OpenAI GPT-4, spaCy, Transformers
- **Voice**: Twilio, AWS Polly
- **Database**: PostgreSQL, MongoDB
- **Cache**: Redis
- **Storage**: AWS S3
- **Testing**: pytest

## API Documentation

API documentation available at:
- Development: `http://localhost:8000/docs`
- Production: `https://api.zecpath.com/docs`

## Contributing

1. Follow the code standards
2. Write tests for new features
3. Update documentation
4. Submit PR for review

## Code Standards

This project follows strict code quality standards. Please read [CODE_STANDARDS.md](CODE_STANDARDS.md) before contributing.

### Quick Commands
```bash
# Format code
black backend/

# Check linting
flake8 backend/

# Run all checks
pre-commit run --all-files
```
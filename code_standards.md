# Zecpath Code Standards & Best Practices

## Python Code Standards

### Style Guide
We follow **PEP 8** - Python's official style guide.

### Key Rules

#### 1. Naming Conventions
```python
# Variables and functions: snake_case
user_name = "John"
def calculate_score():
    pass

# Classes: PascalCase
class CandidateScoring:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRY_ATTEMPTS = 3
API_TIMEOUT = 30

# Private methods: prefix with underscore
def _internal_helper():
    pass
```

#### 2. Indentation & Spacing
- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **88 characters** (Black formatter default)
- Two blank lines between top-level functions/classes
- One blank line between methods

```python
class ATSEngine:
    
    def parse_resume(self, file_path):
        pass
    
    def extract_skills(self, text):
        pass
```

#### 3. Imports
```python
# Standard library imports first
import os
import sys
from datetime import datetime

# Third-party imports second
import pandas as pd
from flask import Flask, request

# Local imports last
from utils.logger import ats_logger
from ats_engine.parser import ResumeParser
```

#### 4. String Formatting
Use f-strings for string formatting:
```python
# Good
name = "John"
message = f"Hello, {name}!"

# Avoid
message = "Hello, " + name + "!"
message = "Hello, {}!".format(name)
```

#### 5. Type Hints
Always use type hints for function parameters and return values:
```python
def calculate_ats_score(
    resume_text: str,
    job_requirements: dict,
    weights: dict = None
) -> float:
    """Calculate ATS score for candidate"""
    pass
```

## Documentation Format

### Google-Style Docstrings

We use **Google-style docstrings** for all functions and classes.

#### Function Documentation
```python
def parse_resume(file_path: str, extract_skills: bool = True) -> dict:
    """
    Parse resume from PDF/DOCX file and extract information.
    
    This function reads a resume file, extracts text content, and
    parses it to identify key information like skills, experience,
    education, and contact details.
    
    Args:
        file_path: Path to the resume file (PDF or DOCX).
        extract_skills: Whether to extract skills automatically.
            Defaults to True.
    
    Returns:
        A dictionary containing parsed resume data with keys:
            - 'name': Candidate name
            - 'email': Email address
            - 'phone': Phone number
            - 'skills': List of extracted skills
            - 'experience': Years of experience
            - 'education': Educational background
    
    Raises:
        FileNotFoundError: If the resume file doesn't exist.
        ValueError: If the file format is not supported.
    
    Example:
        >>> resume_data = parse_resume('/path/to/resume.pdf')
        >>> print(resume_data['name'])
        'John Doe'
    """
    pass
```

#### Class Documentation
```python
class ATSEngine:
    """
    AI-powered Applicant Tracking System engine.
    
    This class handles resume parsing, skill extraction, candidate
    scoring, and automated shortlisting based on job requirements.
    
    Attributes:
        model_name: Name of the AI model used for parsing.
        threshold_score: Minimum score for candidate shortlisting.
        logger: Logger instance for tracking operations.
    
    Example:
        >>> ats = ATSEngine(threshold_score=70)
        >>> score = ats.score_candidate(resume_data, job_requirements)
        >>> print(score)
        85.5
    """
    
    def __init__(self, model_name: str = "gpt-4", threshold_score: int = 70):
        """
        Initialize the ATS Engine.
        
        Args:
            model_name: AI model to use for resume analysis.
            threshold_score: Minimum passing score (0-100).
        """
        self.model_name = model_name
        self.threshold_score = threshold_score
```

## File Organization

### Module Structure
```python
"""
Module: ats_engine/scorer.py
Description: Candidate scoring algorithms for ATS system.
Author: Your Name
Created: 2024-01-20
"""

import logging
from typing import Dict, List, Optional

from utils.logger import ats_logger
from utils.config import Config


class CandidateScorer:
    """Scores candidates based on multiple criteria."""
    
    def __init__(self):
        """Initialize the scorer with default weights."""
        self.logger = ats_logger
        self.weights = self._load_default_weights()
    
    def _load_default_weights(self) -> Dict[str, float]:
        """Load default scoring weights (private method)."""
        return {
            'skills': 0.4,
            'experience': 0.3,
            'education': 0.2,
            'certifications': 0.1
        }
```

## Error Handling

### Standard Pattern
```python
from utils.logger import ats_logger

def process_resume(file_path: str) -> dict:
    """Process resume with proper error handling."""
    try:
        # Main logic
        with open(file_path, 'r') as f:
            content = f.read()
        
        result = parse_content(content)
        ats_logger.info(f"Successfully processed resume: {file_path}")
        return result
        
    except FileNotFoundError:
        ats_logger.error(f"Resume file not found: {file_path}")
        raise
        
    except Exception as e:
        ats_logger.error(f"Error processing resume: {str(e)}")
        raise ValueError(f"Failed to process resume: {str(e)}")
```

## Testing Standards

### Test Naming
```python
class TestATSEngine:
    """Test cases for ATS Engine."""
    
    def test_parse_resume_with_valid_pdf(self):
        """Test resume parsing with valid PDF file."""
        pass
    
    def test_parse_resume_raises_error_for_invalid_file(self):
        """Test that invalid file raises appropriate error."""
        pass
    
    def test_extract_skills_returns_list(self):
        """Test skill extraction returns list of strings."""
        pass
```

### Test Structure
```python
def test_calculate_ats_score():
    """Test ATS score calculation."""
    # Arrange
    resume_data = {
        'skills': ['Python', 'JavaScript'],
        'experience': 3
    }
    job_requirements = {
        'required_skills': ['Python', 'React'],
        'min_experience': 2
    }
    
    # Act
    score = calculate_ats_score(resume_data, job_requirements)
    
    # Assert
    assert 0 <= score <= 100
    assert isinstance(score, (int, float))
```

## Git Commit Standards

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples
```
feat: Add AI voice call retry logic

Implemented automatic retry mechanism for failed AI voice calls
with configurable delay and maximum attempts.

Closes #123
```

```
fix: Resolve resume parsing error for DOCX files

Fixed issue where DOCX files with special characters
were not being parsed correctly.
```

## Code Review Checklist

Before submitting code for review:

- [ ] Code follows PEP 8 style guide
- [ ] All functions have docstrings
- [ ] Type hints are added
- [ ] Error handling is implemented
- [ ] Tests are written and passing
- [ ] Logging is added for important operations
- [ ] No sensitive data in code
- [ ] Code is formatted with Black
- [ ] No linting errors

## Tools Configuration

### Black (Code Formatter)
```bash
# Format all Python files
black backend/

# Check without modifying
black backend/ --check
```

### Flake8 (Linter)
```bash
# Lint all Python files
flake8 backend/

# With specific rules
flake8 backend/ --max-line-length=88 --ignore=E203,W503
```

### Pylint (Advanced Linter)
```bash
# Run pylint
pylint backend/

# With configuration
pylint backend/ --rcfile=.pylintrc
```

## Environment-Specific Rules

### Development
- Debug logging enabled
- Detailed error messages
- Local database connections

### Production
- Minimal logging (INFO level)
- Generic error messages
- Environment variables for secrets
- No print statements

## Security Standards

1. **Never commit sensitive data**
   - API keys go in `.env`
   - Use `.env.example` for templates
   
2. **Input validation**
   - Validate all user inputs
   - Sanitize file uploads
   
3. **SQL injection prevention**
   - Use parameterized queries
   - ORM for database operations

4. **Authentication**
   - JWT tokens for API
   - Secure password hashing

## Performance Guidelines

- Use list comprehensions over loops when possible
- Cache expensive operations
- Use generators for large datasets
- Profile code before optimization
- Database queries: Use indexes, avoid N+1 queries

## Conclusion

Following these standards ensures:
- ✅ Consistent, readable code
- ✅ Easy maintenance and debugging
- ✅ Smooth team collaboration
- ✅ Professional documentation
- ✅ High code quality
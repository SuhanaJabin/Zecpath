import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""

    # Application
    APP_NAME = "Zecpath AI Hiring Platform"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "")

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/zecpath"
    )

    # Redis
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # AWS S3
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "zecpath-storage")

    # AI Settings
    AI_MODEL = os.getenv("AI_MODEL", "gpt-4")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

    # Interview Settings
    MAX_RETRY_ATTEMPTS = int(os.getenv("MAX_RETRY_ATTEMPTS", "3"))
    RETRY_DELAY_MINUTES = int(os.getenv("RETRY_DELAY_MINUTES", "60"))
    OFFICE_HOURS_START = int(os.getenv("OFFICE_HOURS_START", "10"))
    OFFICE_HOURS_END = int(os.getenv("OFFICE_HOURS_END", "18"))

    # Scoring Thresholds
    ATS_PASS_THRESHOLD = int(os.getenv("ATS_PASS_THRESHOLD", "70"))
    HR_PASS_THRESHOLD = int(os.getenv("HR_PASS_THRESHOLD", "65"))
    TECH_PASS_THRESHOLD = int(os.getenv("TECH_PASS_THRESHOLD", "70"))

    # File Upload
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
    ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        required_vars = ["OPENAI_API_KEY", "DATABASE_URL"]

        missing = [var for var in required_vars if not getattr(cls, var)]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

        return True


if __name__ == "__main__":
    print(f"App Name: {Config.APP_NAME}")
    print(f"Version: {Config.VERSION}")
    print(f"Debug Mode: {Config.DEBUG}")
    print(f"AI Model: {Config.AI_MODEL}")
    print(f"Max Retry Attempts: {Config.MAX_RETRY_ATTEMPTS}")

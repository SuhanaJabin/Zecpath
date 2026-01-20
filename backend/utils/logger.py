import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_logger(name, log_file=None, level=logging.INFO):
    """
    Setup logger with file and console handlers

    Args:
        name: Logger name
        log_file: Log file name (optional)
        level: Logging level

    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    simple_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    logger.addHandler(console_handler)

    # File handler
    if log_file is None:
        log_file = f"{name}_{datetime.now().strftime('%Y%m%d')}.log"

    file_path = os.path.join(LOGS_DIR, log_file)
    file_handler = RotatingFileHandler(
        file_path, maxBytes=10 * 1024 * 1024, backupCount=5  # 10MB
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)

    return logger


# Create default loggers for different modules
ats_logger = setup_logger("ats_engine", "ats_engine.log")
screening_logger = setup_logger("screening_ai", "screening_ai.log")
interview_logger = setup_logger("interview_ai", "interview_ai.log")
scoring_logger = setup_logger("scoring", "scoring.log")
api_logger = setup_logger("api", "api.log")


if __name__ == "__main__":
    # Test logging
    test_logger = setup_logger("test")
    test_logger.debug("Debug message")
    test_logger.info("Info message")
    test_logger.warning("Warning message")
    test_logger.error("Error message")
    test_logger.critical("Critical message")

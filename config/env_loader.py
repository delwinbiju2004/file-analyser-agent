import os
from dotenv import load_dotenv


def load_environment():
    """Reads the .env file and loads environment variables into the system."""
    load_dotenv()


def get_api_key():
    """Retrieves the Anthropic API key from the loaded environment variables.
    Provides the API key to other modules that need it."""
    load_environment()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set ANTHROPIC_API_KEY in your .env file.")
    return api_key
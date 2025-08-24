import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from project root
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
VECTOR_DB_URL = os.getenv('VECTOR_DB_URL')

# Add other configs as needed

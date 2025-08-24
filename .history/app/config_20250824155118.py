import os
from dotenv import load_dotenv

# Load .env file automatically
load_dotenv()

# Read environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
VECTOR_DB_URL = os.getenv("VECTOR_DB_URL")

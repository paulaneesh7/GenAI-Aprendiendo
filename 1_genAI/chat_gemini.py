from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

# ✅ Use os.getenv to fetch from .env file
api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Which is the best football team in the world"
)

print(response.text)

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

print("Available Models")

try:
    for model in client.models.list():
        print(model.name)
except Exception as e:
    print("Error:", e)
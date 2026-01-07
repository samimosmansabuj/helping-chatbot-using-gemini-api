from google import genai
from app.config import GEMINI_API_KEY
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
)
print(response)
print("================")
print(response.text)

from google import generativeai
from app.config import GEMINI_API_KEY
from dotenv import load_dotenv
import os
load_dotenv()

generativeai.configure(api_key=GEMINI_API_KEY)
model = generativeai.GenerativeModel(
    model_name=os.getenv("MODEL_NAME"),
    generation_config={
        "temperature": 0.7,
        "top_p": 0.9,
        "max_output_tokens": 1024,
    }
)

# client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt: str, history: list = None):
    try:
        chat = model.start_chat(history=history or [])
        response = chat.send_message(prompt)
        # response = 
        return response.text
    except Exception as e:
        return e

# from google import genai
# from app.config import GEMINI_API_KEY

# client = genai.Client(api_key=GEMINI_API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
# )
# print(response)
# print("================")
# print(response.text)

import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Artificial Intelligence Furure?")
print(response.text)


from google import genai

client = genai.Client(api_key="AIzaSyALEJgn6XgHKobYwSXu3rdCMW2dlyRHeTU")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
    # model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response)
print("================")
print(response.text)

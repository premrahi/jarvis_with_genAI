import google.generativeai as genai
from config import apikey

genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")

# custom prompt
prompt = "You are Jarvis, a helpful AI assistant. Reply politely and keep answers short."
response = model.generate_content(prompt)

print(response.text)
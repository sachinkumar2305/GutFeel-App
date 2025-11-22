import google.generativeai as genai

genai.configure(api_key="AIzaSyBEl6EZw1l0sGMZwTdrVWHE1XxgivqUq5Q")

print("Available Gemini models:")
for model in genai.list_models():
    print(f"- {model.name}")

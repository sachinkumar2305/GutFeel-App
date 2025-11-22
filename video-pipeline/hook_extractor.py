import gspread
from oauth2client.service_account import ServiceAccountCredentials
import google.generativeai as genai
import json

# --- CONFIG ---
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1KYK5knnQm10W5R_RuT-wbzSJWJUWgCHayRypuIBdHWQ/edit?gid=0"
SHEET_NAME = "Sheet1"  # Change if needed
GEMINI_API_KEY = "AIzaSyBEl6EZw1l0sGMZwTdrVWHE1XxgivqUq5Q"

# --- GOOGLE SHEETS AUTH ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\dell\Documents\Healthy-Gut-AI\video-pipeline\google-credentials.json", scope)
gc = gspread.authorize(creds)

# --- EXTRACT HOOKS ---
sh = gc.open_by_url(SPREADSHEET_URL)
worksheet = sh.worksheet(SHEET_NAME)
hooks = worksheet.col_values(1)[1:]  # Skip header

genai.configure(api_key=GEMINI_API_KEY)

def generate_hook_variations(hook, brand="GutFeel"):
    prompt = f"""
    You are a viral video scriptwriter for the GutFeel app. Given the hook: '{hook}', generate 3-5 Veo3-style hook variations. Each should:
    - Highlight gut health improvement
    - Use movement-heavy, cinematic, pattern-interrupt styles
    - Target core personas from the spreadsheet
    - Be short, punchy, and engaging
    - Avoid logos, text overlays, or music references
    Output as a numbered list.
    """
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text

# --- MAIN PIPELINE ---
all_variations = {}
for hook in hooks:
    variations = generate_hook_variations(hook)
    all_variations[hook] = variations

with open("hook_variations.json", "w", encoding="utf-8") as f:
    json.dump(all_variations, f, ensure_ascii=False, indent=2)

print("✅ Hook variations generated and saved to hook_variations.json")

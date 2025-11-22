import json
import requests

# --- CONFIG ---
INPUT_FILE = "veo3_scripts.json"
API_URL = "http://localhost:5000/generate"

# --- LOAD SCRIPTS ---
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    veo3_scripts = json.load(f)

## No headers needed for local API

results = {}
for hook, scripts in veo3_scripts.items():
    results[hook] = []
    for idx, script in enumerate(scripts):
        try:
            prompt = script.get("hook", "")
            output_name = f"{hook}_{idx}.mp4"
            payload = {"prompt": prompt, "output_name": output_name}
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            results[hook].append({"script": script, "response": response.json()})
            print(f"✅ Video generation requested for hook: {hook}")
        except Exception as e:
            print(f"❌ Error generating video for hook: {hook} | {e}")
            results[hook].append({"script": script, "error": str(e)})

with open("video_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("✅ All video results saved to video_results.json")

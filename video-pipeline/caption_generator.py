import json
import openai

# --- CONFIG ---
VIDEO_RESULTS_FILE = "video_results.json"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

openai.api_key = OPENAI_API_KEY

with open(VIDEO_RESULTS_FILE, "r", encoding="utf-8") as f:
    video_results = json.load(f)

captions = {}
for hook, videos in video_results.items():
    captions[hook] = []
    for video in videos:
        script = video.get("script", {})
        hook_text = script.get("hook", "")
        prompt = f"Generate a short, engaging caption for this GutFeel video hook: '{hook_text}'. Focus on gut health improvement and encourage viewers to take action."
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a creative social media copywriter."}, {"role": "user", "content": prompt}]
            )
            caption = response.choices[0].message.content.strip()
            captions[hook].append({"caption": caption, "video_url": video.get("video_url", "")})
        except Exception as e:
            captions[hook].append({"error": str(e), "video_url": video.get("video_url", "")})

with open("video_captions.json", "w", encoding="utf-8") as f:
    json.dump(captions, f, ensure_ascii=False, indent=2)

print("✅ Video captions generated and saved to video_captions.json")

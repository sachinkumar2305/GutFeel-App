import json

# --- CONFIG ---
INPUT_FILE = "hook_variations.json"
OUTPUT_FILE = "veo3_scripts.json"

# Example template for Veo3 JSON
VEO3_TEMPLATE = {
    "camera": {
        "type": "cinematic",
        "movement": "dynamic tracking shot"
    },
    "character": {
        "persona": "GutFeel user",
        "emotion": "hopeful",
        "action": "engaging with gut health tips"
    },
    "lighting": "bright, natural",
    "style": "pattern-interrupt, movement-heavy",
    "dialogue_tone": "friendly, educational",
    "constraints": {
        "no_logos": True,
        "no_text": True,
        "no_music": True
    },
    "brand": "GutFeel",
    "product_benefit": "gut health improvement"
}

# --- LOAD HOOK VARIATIONS ---
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    hook_variations = json.load(f)

veo3_scripts = {}
for hook, variations in hook_variations.items():
    # Split variations into list if needed
    if isinstance(variations, str):
        variations_list = [v.strip() for v in variations.split('\n') if v.strip()]
    else:
        variations_list = variations
    veo3_scripts[hook] = []
    for variation in variations_list:
        script = VEO3_TEMPLATE.copy()
        script["hook"] = variation
        veo3_scripts[hook].append(script)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(veo3_scripts, f, ensure_ascii=False, indent=2)

print(f"✅ Veo3 JSON scripts generated and saved to {OUTPUT_FILE}")

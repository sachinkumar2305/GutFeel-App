# GutFeel AI Video Content Generation Pipeline

## Pipeline Steps
1. **Hook Extraction & Variation Generation**
   - `hook_extractor.py`: Extracts hooks from Google Spreadsheet and generates 3-5 Veo3-style hook variations using ChatGPT. Output: `hook_variations.json`
2. **JSON Script Generation**
   - `veo3_json_generator.py`: Converts hook variations to Veo3 JSON format with camera, character, style, and constraints. Output: `veo3_scripts.json`
3. **Video Generation & Batch Processing**
   - `veo3_api_client.py`: Integrates with Veo3 API to generate videos for each script. Output: `video_results.json`

## Usage
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run each step in order:
   ```
   python hook_extractor.py
   python veo3_json_generator.py
   python veo3_api_client.py
   ```
3. Review outputs in JSON files for hooks, scripts, and video URLs/errors.

## Customization
- Update templates in `veo3_json_generator.py` for camera, character, style, etc.
- Add your API keys in the respective scripts.
- Adjust batch size or error handling as needed.

## Next Steps
- Implement A/B testing and performance tracking
- Optimize outputs for Meta/Instagram ads
- Add automated caption generation and multi-platform adaptation

## License
MIT

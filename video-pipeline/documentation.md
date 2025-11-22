# GutFeel AI Video Content Generation Pipeline Documentation

## Overview
This pipeline automates the creation of viral video content for the GutFeel app using hooks from a Google Spreadsheet, ChatGPT for creative variations, and Veo3 API for video generation.

## Steps
1. **Hook Extraction & Variation Generation**
   - `hook_extractor.py`: Extracts hooks and generates 3-5 Veo3-style variations per hook using ChatGPT.
   - Output: `hook_variations.json`
2. **JSON Script Generation**
   - `veo3_json_generator.py`: Converts hook variations to Veo3 JSON scripts (camera, character, style, constraints).
   - Output: `veo3_scripts.json`
3. **Video Generation & Batch Processing**
   - `veo3_api_client.py`: Sends scripts to Veo3 API, retrieves video URLs, and logs errors.
   - Output: `video_results.json`
4. **Prompt Engineering**
   - See `prompt_engineering.md` for templates and guidance.
5. **Video Variation Strategy**
   - See `video_variation_strategy.md` for content types and implementation.
6. **Rapid Testing Framework**
   - See `rapid_testing_framework.md` for batch testing and performance tracking.

## Outputs
- Hook variations JSON
- Veo3 JSON scripts
- Video results JSON (URLs/errors)
- Documentation and templates for prompt engineering, variation strategy, and testing

## Demo Video
- Use generated video URLs to compile a demo reel for GutFeel

## JSON Template Library
- See `veo3_json_generator.py` for reusable script templates

## Error Handling
- All scripts include try/except blocks and log errors in output files

## Batch Processing
- Scripts process multiple hooks and variations in one run

## Optimization
- Outputs are suitable for Meta/Instagram ad formats
- Easily adaptable for TikTok, YouTube Shorts

## License
MIT

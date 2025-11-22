# GutFeel AI Video Content Generation Pipeline

## Overview
Automated pipeline to generate viral video hooks and Veo3-style variations for the GutFeel app using Google Sheets, ChatGPT, and open-source Mochi for local video generation.

## Why We Use Open Source Mochi Instead of Paid API Text-to-Video
We chose Mochi, an open-source video generation library, over paid text-to-video APIs for several reasons:
- **Cost Efficiency:** No recurring fees or usage-based costs, making it ideal for large-scale or frequent video generation.
- **Privacy & Security:** All video generation happens locally, so sensitive data and creative assets never leave your environment.
- **Customization:** Full access to the codebase allows us to tailor video generation workflows and experiment with new features.
- **No API Limits:** Avoids rate limits, quotas, and downtime associated with third-party services.
- **Community & Transparency:** Open-source projects benefit from community contributions, peer review, and rapid innovation.

## Features
- Extract hooks from Google Spreadsheet
- Generate 3-5 Veo3-style hook variations per hook using ChatGPT
- Output results to JSON for further processing
- (With Mochi) Generate videos locally from JSON scripts

## Setup Instructions
### Prerequisites
- Python 3.8+
- Google Sheets API credentials (`google-credentials.json`)
- OpenAI API key
- Mochi library (see `../mochi/README.md` for setup)

### Installation
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place your `google-credentials.json` in the project folder
4. Add your OpenAI API key in `hook_extractor.py`
5. Set up Mochi by following the instructions in the `mochi` folder

### Usage
Run the extractor:
```
python hook_extractor.py
```
- Outputs `hook_variations.json` with hooks and generated variations

To generate videos using Mochi:
```
python ../mochi/mochi_api.py
python veo3_api_client.py
```
- Outputs videos and results in `api_output/` and `video_results.json`

## Next Steps
- Convert approved hooks to Veo3 JSON format
- Integrate Veo3 API for video generation (optional)
- Batch process and optimize outputs for Meta/Instagram ads

## License
MIT

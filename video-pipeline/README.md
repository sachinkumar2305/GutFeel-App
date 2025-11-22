# GutFeel AI Video Content Generation Pipeline

## Overview
Automated pipeline to generate viral video hooks and Veo3-style variations for GutFeel app using Google Sheets and ChatGPT.

## Features
- Extract hooks from Google Spreadsheet
- Generate 3-5 Veo3-style hook variations per hook using ChatGPT
- Output results to JSON for further processing

## Setup Instructions
### Prerequisites
- Python 3.8+
- Google Sheets API credentials (`google-credentials.json`)
- OpenAI API key

### Installation
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Place your `google-credentials.json` in the project folder
4. Add your OpenAI API key in `hook_extractor.py`

### Usage
Run the extractor:
```
python hook_extractor.py
```
- Outputs `hook_variations.json` with hooks and generated variations

## Next Steps
- Convert approved hooks to Veo3 JSON format
- Integrate Veo3 API for video generation
- Batch process and optimize outputs for Meta/Instagram ads

## License
MIT

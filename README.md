# ResuAIze - AI-Powered Resume Analysis Tool

ResuAIze is a Streamlit-based application designed to assist candidates and recruiters with intelligent resume evaluation. Leveraging Google's Gemini API and OCR technology, this tool performs advanced resume reviews, grammar and spelling checks, ATS percentage matching, and skill gap analysis based on job descriptions.

## Features

- Resume Review: Get a detailed professional evaluation of a resume against a job description.
- ATS Percentage Match: Simulate an ATS system and receive a match percentage along with missing keywords.
- Skill Gap Learning Plan: Identify missing technical/soft skills and get a personalized learning path to bridge gaps.
- OCR-based Grammar & Spelling Check: Extract text from PDF resumes and detect grammatical, spelling, and sentence structure issues.

## Tech Stack

- Streamlit: Interactive web interface
- Google Gemini API: For AI-powered resume analysis
- pytesseract: OCR for extracting text from PDFs
- pdf2image: Convert PDFs to images for OCR processing
- spaCy: Named Entity Recognition to filter false positives during grammar checks
- language_tool_python: Grammar and spelling corrections

## How it Works

1. Upload a resume (PDF format).
2. Provide a job description.
3. Select from the following options:
   - Resume Review
   - ATS Percentage Match
   - Skill Gap Learning Plan
   - Grammar & Spelling Check
4. The application processes the resume, analyzes it against the job description, and provides actionable feedback.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/resuaize.git
   cd resuaize
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Create a `.env` file and add your Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Folder Structure

```
/resuaize
│
├── app.py                  # Streamlit application
├── ocr_utils.py            # OCR extraction & grammar checking logic
├── prompts.py              # Gemini API prompts
├── requirements.txt        # Python dependencies
└── .env.example            # Example environment file
```

## Notes

- Ensure that Tesseract OCR is installed and available in your system PATH.
- This tool is designed to help candidates enhance their resumes and prepare better for job applications.

## Author

Developed by Aditya Patel

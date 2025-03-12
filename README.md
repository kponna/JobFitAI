# JobFitAI: AI-Powered Resume Analyzer

## Overview
JobFitAI is an AI-powered resume analysis tool that helps job seekers optimize their resumes for specific job descriptions. It utilizes DeepSeek-R1 via DeepInfra to extract key skills, experiences, and qualifications from resumes and provides actionable feedback to improve job alignment. The project features a Gradio-based web interface that allows users to upload resumes in PDF or audio format and receive structured analysis and recommendations.

Checkout the detailed guide on this project at 

## Features
- **AI-driven resume analysis** using DeepSeek-R1 on DeepInfra
- **PDF and Audio resume support** with automated text extraction
- **Skill and experience matching** against job descriptions
- **Match scoring and feedback generation** for improving resume alignment
- **Interactive web UI** built with Gradio

## Folder Structure
```
JobFitAI/
│── src/                # Source code for resume analysis
│   ├── __pycache__/    # Compiled Python files
│   ├── analyzer.py     # Calls DeepSeek-R1 for resume analysis
│   ├── audio_transcriber.py  # Converts audio resumes to text
│   ├── feedback_generator.py # Generates resume improvement feedback
│   ├── pdf_extractor.py  # Extracts text from PDF resumes
│   ├── resume_pipeline.py # Manages resume processing
│── .env                 # Environment variables (API keys)
│── .gitignore           # Git ignore file
│── app.py               # Gradio web interface
│── LICENSE              # License information
│── README.md            # Documentation (this file)
│── requirements.txt     # Python dependencies
```

## Installation
### Prerequisites
Ensure you have Python installed (3.8+ recommended) and set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file and add your DeepInfra API key:
```
DEEPINFRA_TOKEN=your_api_key_here
```

## Usage
### Running the Application
To launch the Gradio web interface, run:
```bash
python app.py
```
This starts a local web server where you can upload resumes and get AI-generated feedback.

### How It Works
1. **Upload a Resume (PDF/Audio).**
2. **Paste a Job Description.**
3. **Click Submit** to analyze the resume.
4. **View the Analysis & Recommendations.**

## Technologies Used
- **DeepSeek-R1** (via DeepInfra API) for AI-driven resume analysis
- **Gradio** for building an interactive UI
- **OpenAI Whisper** for audio transcription
- **PyPDF2** for extracting text from PDFs

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing
Feel free to fork the repo and submit pull requests. Suggestions and improvements are welcome!

## Contact
For questions or support, please reach out to the project maintainers.


 

# AI English Compliance Checker

This project checks English grammar/style in PDF or DOCX files using an AI agent.

## Features
- Upload document via API
- Grammar/style check
- Auto-correct and download fixed file

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## API Endpoints
- `POST /upload` – Upload a document, returns compliance issues
- `POST /correct` – Upload a document, returns corrected file

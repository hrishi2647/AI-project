from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.file_utils import extract_text
from app.ai_agent import check_guidelines, correct_text
from app.modifier import save_docx
import tempfile
import os

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files are allowed.")

    text = extract_text(file)
    issues = check_guidelines(text)
    return {"issues_found": issues, "preview": text[:500]}


@router.post("/correct/")
async def correct_file(file: UploadFile = File(...)):
    text = extract_text(file)
    corrected = correct_text(text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    save_docx(corrected, temp_file.name)
    return FileResponse(temp_file.name, filename="corrected.docx", media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

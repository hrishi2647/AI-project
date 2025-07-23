import fitz  # PyMuPDF
import docx

def extract_text(file):
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=file.file.read(), filetype="pdf")
        return " ".join([page.get_text() for page in doc])
    elif file.filename.endswith(".docx"):
        docx_file = docx.Document(file.file)
        return "\n".join([para.text for para in docx_file.paragraphs])
    else:
        return ""

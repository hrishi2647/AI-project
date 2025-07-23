from docx import Document

def save_docx(text: str, filename: str):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)

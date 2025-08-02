import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    # Split by paragraphs instead of fixed chars
    paragraphs = re.split(r'\n{2,}', text)
    chunks = [p.strip() for p in paragraphs if len(p.strip()) > 50]
    return chunks

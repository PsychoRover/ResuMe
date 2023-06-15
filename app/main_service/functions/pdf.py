import re

import PyPDF2
from fastapi import HTTPException
from PyPDF2.errors import PdfReadError


def parse_pdf(pdf_file) -> tuple[str, str, str]:
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
    except PdfReadError:
        raise HTTPException(status_code=404, detail="Oops.. wrong file format")
    
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()

    name: str = re.findall(r"([A-Z][a-z]+ [A-Z][a-z]+)", text)[0]
    email: str = re.findall(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+", text)[0]

    return text, name, email

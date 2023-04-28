import PyPDF2
import re
import json
import json
def parse_pdf(pdf_file) -> str:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()

    # Extract name and email
    name = re.findall(r"([A-Z][a-z]+ [A-Z][a-z]+)", text)
    email = re.findall(r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+", text)

    return text, name[0], email[0]



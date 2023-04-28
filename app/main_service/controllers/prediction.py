import requests
from PyPDF2.errors import PdfReadError
from fastapi import APIRouter, UploadFile, File

from app.main_service.functions import parse_pdf

router = APIRouter(prefix="/v1")


@router.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    try:
        cv_text = parse_pdf(pdf_file.file)
    except PdfReadError:
        return "Wrong file extension, please upload .PDF or .DOCX"
    response = requests.post("http://localhost:8000/predict", json=[cv_text], timeout=10)
    assurance, category = response.json()
    return {"prediction": category}

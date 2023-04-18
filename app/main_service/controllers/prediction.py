import requests
from fastapi import APIRouter, UploadFile, File

from app.main_service.functions import parse_pdf

router = APIRouter(prefix="/v1")


@router.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    cv_text = parse_pdf(pdf_file.file)
    response = requests.post("http://localhost:8000/predict", json=[cv_text])
    assurance, category = response.json()
    return {"prediction": category}

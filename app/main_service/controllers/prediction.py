import requests
from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from functions import parse_pdf



router = APIRouter(prefix="/v1")
templates = Jinja2Templates(directory="templates")

@router.post("/upload", response_class=HTMLResponse)
async def upload_pdf(request: Request, pdf_file: UploadFile = File(...)):
    cv_text, name, email = parse_pdf(pdf_file.file)
    response = requests.post("http://localhost:8000/predict", json=[cv_text], timeout=10)
    assurance, category = response.json()
    assurance = round(assurance, 2)
    return templates.TemplateResponse("prediction.html", {"request": request, "prediction": category, "assurance": assurance,"name": name, "email": email})
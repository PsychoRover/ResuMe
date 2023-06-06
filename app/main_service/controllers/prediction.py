import requests
from PyPDF2.errors import PdfReadError
from fastapi import APIRouter, UploadFile, File, Request
from starlette.templating import Jinja2Templates

from app.main_service.functions import parse_pdf
from constants import ENDPOINT

router = APIRouter(prefix="/v1")
templates = Jinja2Templates(directory="templates")


@router.post("/upload")
async def upload_pdf(request: Request, pdf_file: UploadFile = File(...)):
    try:
        cv_text, name, email = parse_pdf(pdf_file.file)
    except PdfReadError:
        return "Wrong file extension, please upload .PDF or .DOCX"
    response = requests.post(
        ENDPOINT,
        json=[cv_text],
    )
    assurance, category = response.json()
    return templates.TemplateResponse("prediction.html",
                                      {"request": request, "prediction": category, "assurance": f"{assurance:.2f}",
                                       "name": name,
                                       "email": email})

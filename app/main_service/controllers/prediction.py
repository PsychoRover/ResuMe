import requests
from fastapi import APIRouter, File, Request, UploadFile
from PyPDF2.errors import PdfReadError
from starlette.templating import Jinja2Templates

from ..constants import ENDPOINT, Folders, chat_prompt
from ..functions.openai import extract_skills, llm
from ..functions.pdf import parse_pdf

router = APIRouter(prefix="/v1")
templates = Jinja2Templates(directory=Folders.TEMPLATES)


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

    model_response = llm.predict(chat_prompt(category, cv_text))

    relevant_skills, missing_skills = extract_skills(model_response)

    return templates.TemplateResponse(
        "prediction.html",
        {
            "request": request,
            "prediction": category,
            "assurance": f"{assurance:.2f}",
            "name": name,
            "email": email,
            "relevant_skills": relevant_skills,
            "missing_skills": missing_skills,
        },
    )

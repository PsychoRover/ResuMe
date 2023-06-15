from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse

from ..functions.parser import analyzer_resolver

router = APIRouter(prefix="/v1")


@router.post("/upload", response_class=HTMLResponse)
async def upload_pdf(
    request: Request, user_type: str = Form(...), pdf_file: UploadFile = File(...)
):
    return analyzer_resolver.get(user_type)(request, pdf_file)

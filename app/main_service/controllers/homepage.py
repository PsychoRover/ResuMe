from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.main_service.constants import Folders

router = APIRouter()

# ------- Templates ------- #
templates = Jinja2Templates(directory=Folders.TEMPLATES)


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/analyzer", response_class=HTMLResponse)
async def start(request: Request):
    return templates.TemplateResponse("analyzer.html", {"request": request})

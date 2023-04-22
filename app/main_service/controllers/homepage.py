from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# ------- Templates ------- #
templates = Jinja2Templates(directory="templates")


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@router.get("/analyzer", response_class=HTMLResponse)
async def start(request: Request):
    return templates.TemplateResponse("analyzer.html", {"request": request})

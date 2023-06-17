from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from ..templates import About, Analyzer, ContactUs, Homepage

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return Homepage(context={"request": request})


@router.get("/analyzer", response_class=HTMLResponse)
async def start(request: Request):
    return Analyzer(context={"request": request})


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return About(context={"request": request})


@router.get("/contact-us", response_class=HTMLResponse)
async def contact_us(request: Request):
    return ContactUs(context={"request": request})

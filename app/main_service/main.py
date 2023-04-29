from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from controllers import prediction, homepage

# ------- App Configurations ------- #
app = FastAPI(debug=True, tilte="ResuMe")
app.include_router(prediction.router)
app.include_router(homepage.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ------- Templates ------- #
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

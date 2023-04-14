from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from controller import evaluation

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(evaluation.router)


@app.get("/", response_class=HTMLResponse)
async def read_html(request: Request):
    # with open("templates/homepage.html", "r") as f:
    #     html_content = f.read()
    return templates.TemplateResponse("homepage.html", {"request": request, "id": id})


@app.get("/items/{id}")
async def get_items(id: int):
    return {"item": id}

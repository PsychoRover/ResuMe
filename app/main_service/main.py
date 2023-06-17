from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.main_service.constants import Folders
from app.main_service.controllers import homepage, prediction

# ------- App Configurations ------- #
app = FastAPI(debug=True, title="ResuMe")
app.include_router(prediction.router)
app.include_router(homepage.router)
app.mount("/static", StaticFiles(directory=Folders.STATIC), name="static")

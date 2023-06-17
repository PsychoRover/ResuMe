from functools import partial
from typing import Any, Callable, Dict

from starlette.templating import Jinja2Templates, _TemplateResponse

from .constants import Folders

Context = Dict[str, Any]
Template = Callable[[Context], _TemplateResponse]

templates = Jinja2Templates(directory=Folders.TEMPLATES)

_response = templates.TemplateResponse

Homepage: Template = partial(_response, name=f"templates/homepage.html")

About: Template = partial(_response, name=f"templates/about.html")

Analyzer: Template = partial(_response, name=f"templates/analyzer.html")

Prediction: Template = partial(_response, name=f"templates/prediction.html")

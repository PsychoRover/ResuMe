from functools import partial
from typing import Any, Callable, Dict

from starlette.templating import Jinja2Templates, _TemplateResponse

from ..constants import Folders

Context = Dict[str, Any]
Template = Callable[[Context], _TemplateResponse]


templates = Jinja2Templates(directory=Folders.TEMPLATES)

_response = templates.TemplateResponse

Homepage: Template = partial(_response, name="homepage.html")

About: Template = partial(_response, name="about.html")

Analyzer: Template = partial(_response, name="analyzer.html")

CandidatePrediction: Template = partial(_response, name="prediction.html")

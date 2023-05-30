import typing

import transformers as tr
from fastapi import FastAPI
from loguru import logger

from app.model_service.functions import get_classes

classes = get_classes("./classes.toml")

logger.info(" ---- Loading Model ----")
pipe = tr.pipeline(task="zero-shot-classification", model="roberta-large-mnli")
logger.info(" ---- Done Loading Model ----")

app = FastAPI()


@app.post("/predict")
async def predict(cv: list[str]) -> typing.Tuple[float, str]:
    raw_prediction = pipe(cv[0], candidate_labels=classes)
    return max(zip(raw_prediction["scores"], raw_prediction["labels"]))

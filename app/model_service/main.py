import typing

import tensorflow as tf
from fastapi import FastAPI

from app.model_service.functions import get_classes

if typing.TYPE_CHECKING:
    from keras import Model
    from numpy import ndarray

classes = get_classes("./classes.toml")
model: "Model" = tf.keras.models.load_model("./model")

app = FastAPI()


@app.post("/predict")
def predict(cv: list[str]) -> tuple[float, str]:
    raw_prediction: "ndarray" = model.predict(cv).squeeze()
    prediction = max(zip(raw_prediction, classes))
    return prediction

import numpy as np

from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel, ValidationError, validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .ml.model_mnist import Model, get_model, n_features


class PredictRequest(BaseModel):
    data: List[List[List[List[float]]]]

    # @validator("data")
    # def check_dimensionality(cls, v):
    #     for point in v:
    #         if len(point) != n_features:
    #             raise ValueError(f"Each data point must contain {n_features} features")
    #
    #     return v


class PredictResponse(BaseModel):
    data: List[List[float]]


app = FastAPI()


@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest, model: Model = Depends(get_model)):
    X = np.array(input.data)
    y_pred = model.predict(X)
    result = PredictResponse(data=y_pred.tolist())

    return result


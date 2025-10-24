from fastapi import APIRouter
from app.models.schemas import InputData, TransformedData
from app.services.transformer import transform_data
import requests
import os
import logging
from typing import Any, Dict

router = APIRouter(prefix="/transform", tags=["transform"])

DOWNSTREAM_URL = os.getenv("DOWNSTREAM_URL", "https://httpbin.org/post")

@router.post("/", response_model=Any)
def transform_and_send(data: InputData):
    # logging.info(f"incoming data: {data.model_dump()}")
    print(f"incoming data: {data.model_dump()}")
    # transformed = transform_data(data.model_dump())
    transformed = {}
    return transformed
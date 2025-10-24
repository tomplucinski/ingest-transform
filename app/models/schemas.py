from pydantic import BaseModel
from typing import Any, Dict

class InputData(BaseModel):
    source: str
    payload: Dict[str, Any]

class TransformedData(BaseModel):
    target: str
    mapped: Dict[str, Any]
    
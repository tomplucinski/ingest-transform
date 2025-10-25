import logging

from fastapi import FastAPI

from .api.routes import router

app = FastAPI(
    title="Data Transformer API",
    description="A simple microservice for ingesting JSON, transforming it, and sending to downstream clients.",
    version="1.0.0"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name="uvicorn")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Data Transformer API is running"}

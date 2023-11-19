import uvicorn
from fastapi import FastAPI

from config import AppConfig
from src.dataclasses.api import Payload, ResponseItem

app = FastAPI()


@app.post("/productionplan/")
def calculate_production_plan(payload: Payload) -> list[ResponseItem]:
    pass


if __name__ == "__main__":
    cfg = AppConfig()
    uvicorn.run('main:app', host=cfg.host, port=cfg.port, reload=cfg.debug)
import uvicorn
from fastapi import FastAPI

from config import AppConfig
from src.data_models.api import Payload, ResponseItem
from src.services.production_planner import ProductionPlanner

app = FastAPI()


@app.post("/productionplan")
async def calculate_production_plan(payload: Payload) -> list[ResponseItem]:
    planner = ProductionPlanner(
        supply=payload.get_fuels(), plants=payload.powerplants
        )
    return await planner.plan(payload.load)


if __name__ == "__main__":
    cfg = AppConfig()
    uvicorn.run('main:app', host=cfg.host, port=cfg.port, reload=cfg.debug)
from pydantic import BaseModel, Field

from src.dataclasses.plant import PowerPlant


class Payload(BaseModel):
    class Fuels(BaseModel):
        gas: float = Field(..., alias='gas(euro/MwH)')
        kerosine: float = Field(..., alias='kerosine(euro/MwH)')
        co2: float = Field(..., alias='co2(euro/ton)')
        wind: float = Field(..., alias='wind(%)')
    
    load: int
    fuels: Fuels
    powerplants: list[PowerPlant]


class ResponseItem(BaseModel):
    name: str
    p: float
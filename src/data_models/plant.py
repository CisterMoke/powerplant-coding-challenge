from enum import Enum

from pydantic import BaseModel


class PlantType(str, Enum):
    GASFIRED = 'gasfired'
    TURBOJET = 'turbojet'
    WINDTURBINE = 'windturbine'


class PowerPlant(BaseModel):
    name: str
    type: PlantType
    efficiency: float
    pmin: int
    pmax: int
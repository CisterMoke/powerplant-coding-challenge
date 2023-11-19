from enum import Enum

from pydantic import BaseModel

from src.data_models.fuel import FuelType

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
    fuel_map: dict[PlantType, FuelType] = {
        PlantType.GASFIRED: FuelType.GAS,
        PlantType.TURBOJET: FuelType.KEROSINE,
        PlantType.WINDTURBINE: FuelType.WIND
    }

    def get_fuel_type(self) -> FuelType:
        return self.fuel_map[self.type]

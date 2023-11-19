from enum import Enum

from pydantic import BaseModel


class FuelType(str, Enum):
    GAS = 'gas'
    KEROSINE = 'kerosine'
    CO2 = 'co2'
    WIND = 'wind'


class FuelUnit(str, Enum):
    EUROMWH = 'euro/MWh'
    EUROTON = 'euro/ton'
    PERCENT = '%'


class FuelSupply(BaseModel):
    type: FuelType
    unit: FuelUnit
    cost: float
    available: float
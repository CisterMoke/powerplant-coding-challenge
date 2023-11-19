from enum import Enum

from pydantic import BaseModel


class FuelType(str, Enum):
    GAS = 'gas'
    KEROSINE = 'kerosine'
    CO2 = 'co2'
    WIND = 'wind'


class FuelUnit(str, Enum):
    EUROMWH = 'euro/MwH'
    EUROTON = 'euro/ton'
    PERCENT = '%'


class Fuel(BaseModel):
    type: FuelType
    unit: FuelUnit
    amount: float
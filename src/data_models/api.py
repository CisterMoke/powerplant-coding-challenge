import re
from pydantic import BaseModel, Field

from src.data_models.fuel import Fuel, FuelType, FuelUnit
from src.data_models.plant import PowerPlant
from src.utils.regex import fuel_pattern


class Payload(BaseModel):
    class Fuels(BaseModel):
        gas: float = Field(..., alias='gas(euro/MWh)')
        kerosine: float = Field(..., alias='kerosine(euro/MWh)')
        co2: float = Field(..., alias='co2(euro/ton)')
        wind: float = Field(..., alias='wind(%)')
    
    load: int
    fuels: Fuels
    powerplants: list[PowerPlant]

    def get_fuels(self) -> list[Fuel]:
        all_fuels: list[Fuel] = []
        for field_name, field_info in self.fuels.model_fields.items():
            f_type, f_unit = re.match(fuel_pattern, field_info.alias).groups()
            f_amount = getattr(self.fuels, field_name)
            all_fuels.append(Fuel(type=f_type, unit=f_unit, amount=f_amount))
        return all_fuels


class ResponseItem(BaseModel):
    name: str
    p: float
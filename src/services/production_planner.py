from src.data_models.api import ResponseItem
from src.data_models.fuel import FuelSupply, FuelType
from src.data_models.plant import PowerPlant, PlantType


class ProductionPlanner:
    merit_order: dict[PlantType, int] = {
        PlantType.WINDTURBINE: 0,
        PlantType.GASFIRED: 1,
        PlantType.TURBOJET: 2
    }

    def __init__(self, supply: list[FuelSupply], plants: list[PowerPlant]) -> None:
        self.supply: dict[FuelType, FuelSupply] = {f.type: f for f in supply}
        self.plants: list[PowerPlant] = plants
        self.plants.sort(key=lambda x: self.merit_order[x.type])

    async def plan(self, load: int) -> list[ResponseItem]:
        attained: float = 0
        plan: list[tuple(PowerPlant, float)] = []
        for plant in self.plants:
            remaining = load - attained
            if remaining == 0:
                plan.append((plant, 0))
                continue

            available = self.supply[plant.get_fuel_type()].available
            if plant.type == PlantType.WINDTURBINE:
                pmax = plant.pmax * plant.efficiency * available
                pmin = plant.pmin * plant.efficiency * available
            else:
                pmax, pmin = plant.pmax, plant.pmin

            if pmax <= remaining:
                attained += pmax
                power = pmax
            elif pmin <= remaining:
                attained += remaining
                power = remaining
            else:
                power = 0
            
            plan.append((plant, power))

        return[ResponseItem(name=plant.name, p=round(power, 1))
               for plant, power in plan]
from dataclasses import dataclass


from .Car import Car


@dataclass
class Cargo(Car):
    tonnage: float
    tank_volume: float
    axles_amount: int
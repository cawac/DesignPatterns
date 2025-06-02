from dataclasses import dataclass


from .car import Car


@dataclass
class Cargo(Car):
    tonnage: float
    tank_volume: float
    axles_amount: int
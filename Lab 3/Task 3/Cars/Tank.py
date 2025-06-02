from dataclasses import dataclass


from .Car import Car


@dataclass
class Tank(Car):
    projectile_caliber: float
    shots_per_minute: int
    crew_size: int
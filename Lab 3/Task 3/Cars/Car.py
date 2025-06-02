from abc import ABC
from dataclasses import dataclass


@dataclass
class Car(ABC):
    name: str
    weight: float
    length: float
    max_speed: float
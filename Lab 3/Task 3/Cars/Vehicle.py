from dataclasses import dataclass
from enum import Enum


from .Car import Car


class EColor(Enum):
    """Color enumeration for vehicles."""
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    ORANGE = 4

class EWheelDriveType(Enum):
    """Wheel drive type enumeration for vehicles."""
    NONE = 0
    FRONT = 1
    BACK = 2
    ALL = 3

class EVehicleClass(Enum):
    """Vehicle class enumeration."""
    NONE = 0
    HATCHBACK = 1
    SEDAN = 2
    COUPE = 4 


@dataclass
class Vehicle(Car):
    wheel_drive_type: EWheelDriveType
    vehicle_class: EVehicleClass
    color: EColor
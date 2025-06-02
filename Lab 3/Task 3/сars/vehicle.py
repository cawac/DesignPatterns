from dataclasses import dataclass
from enum import StrEnum
from .car import Car


class EColor(StrEnum):
    """Color enumeration for vehicles."""
    NONE = "none"
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    ORANGE = "orange"


class EWheelDriveType(StrEnum):
    """Wheel drive type enumeration for vehicles."""
    NONE = "none"
    FRONT = "front"
    BACK = "back"
    ALL = "all"


class EVehicleClass(StrEnum):
    """Vehicle class enumeration."""
    NONE = "none"
    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    COUPE = "coupe"


@dataclass
class Vehicle(Car):
    wheel_drive_type: EWheelDriveType
    vehicle_class: EVehicleClass
    color: EColor



@dataclass
class Vehicle(Car):
    wheel_drive_type: EWheelDriveType
    vehicle_class: EVehicleClass
    color: EColor
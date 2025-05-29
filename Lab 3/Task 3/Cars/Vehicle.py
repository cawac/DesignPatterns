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


class Vehicle(Car):
    def __init__(self, name: str, weight: float, length: float, max_speed: float,
                 wheel_drive_type: EWheelDriveType = EWheelDriveType.NONE,
                 vehicle_class: EVehicleClass = EVehicleClass.NONE,
                 color: EColor = EColor.NONE) -> None:
        super().__init__(name, weight, length, max_speed)
        self.wheel_drive_type: EWheelDriveType = wheel_drive_type
        self.vehicle_class: EVehicleClass = vehicle_class
        self.color: EColor = color

    def __repr__(self) -> str:
        return (f"Vehicle(name='{self.name}', weight={self.weight}, length={self.length}, "
                f"max_speed={self.max_speed}, wheel_drive_type={self.wheel_drive_type.name}, "
                f"vehicle_class={self.vehicle_class.name}, color={self.color.name})") 
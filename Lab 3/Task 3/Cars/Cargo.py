from .Car import Car

class Cargo(Car):
    def __init__(self, name: str, weight: float, length: float, max_speed: float,
                 tonnage: float, tank_volume: float, axles_amount: int) -> None:
        super().__init__(name, weight, length, max_speed)
        self.tonnage: float = tonnage
        self.tank_volume: float = tank_volume
        self.axles_amount: int = axles_amount

    def __repr__(self) -> str:
        return (f"Cargo(name='{self.name}', weight={self.weight}, length={self.length}, "
                f"max_speed={self.max_speed}, tonnage={self.tonnage}, "
                f"tank_volume={self.tank_volume}, axles_amount={self.axles_amount})") 
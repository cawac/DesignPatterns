from .Car import Car

class Tank(Car):
    def __init__(self, name: str, weight: float, length: float, max_speed: float,
                 projectile_caliber: float, shots_per_minute: int, crew_size: int) -> None:
        super().__init__(name, weight, length, max_speed)
        self.projectile_caliber: float = projectile_caliber
        self.shots_per_minute: int = shots_per_minute
        self.crew_size: int = crew_size

    def __repr__(self) -> str:
        return (f"Tank(name='{self.name}', weight={self.weight}, length={self.length}, "
                f"max_speed={self.max_speed}, projectile_caliber={self.projectile_caliber}, "
                f"shots_per_minute={self.shots_per_minute}, crew_size={self.crew_size})") 
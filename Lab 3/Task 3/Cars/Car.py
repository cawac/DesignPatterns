from abc import ABC

class Car(ABC):
    def __init__(self, name: str, weight: float, length: float, max_speed: float) -> None:
        self.name: str = name
        self.weight: float = weight
        self.length: float = length
        self.max_speed: float = max_speed

    def __repr__(self) -> str:
        return f"Car(name='{self.name}', weight={self.weight}, length={self.length}, max_speed={self.max_speed})" 
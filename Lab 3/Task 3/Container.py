from abc import ABC, abstractmethod
from typing import List


from Cars.Car import Car
from Observer import Observer


class BaseContainer(ABC):
    @abstractmethod
    def add_car(self, car: Car) -> None:
        pass

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self, car: Car, msg: str) -> None:
        pass

    @abstractmethod
    def update_car(self, car: Car, **changes: dict) -> None:
        pass


class Container(BaseContainer):
    def __init__(self) -> None:
        self.cars: List[Car] = []
        self.observers: List[Observer] = []

    def add_car(self, car: Car) -> None:
        if all(existing_car is not car for existing_car in self.cars):
            self.cars.append(car)
            self.notify_observers(car, "added to the container")

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, car: Car, msg: str) -> None:
        for observer in self.observers:
            observer.update(car, msg)

    def update_car(self, car: Car, **changes: dict) -> None:
        if all(existing_car is not car for existing_car in self.cars):
            print("Car is not in the container.")
            return

        for attr, new_value in changes.items():
            if hasattr(car, attr):
                old_value = getattr(car, attr)
                if old_value != new_value:
                    setattr(car, attr, new_value)
                    msg = f"Property '{attr}' changed from {old_value} to {new_value}"
                    self.notify_observers(car, msg)
            else:
                print(f"Attribute '{attr}' does not exist on {car.__class__.__name__}")
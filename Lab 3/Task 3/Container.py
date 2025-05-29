from typing import List
from Cars.Car import Car
from Observer import Observer

class Container:
    def __init__(self) -> None:
        self.cars: List[Car] = []
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, car: Car) -> None:
        for observer in self.observers:
            observer.update(car)

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
        self.notify_observers(car) 
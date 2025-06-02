from abc import ABC, abstractmethod


from сars.car import Car


class Observer(ABC):
    _id_counter: int = 1

    def __init__(self) -> None:
        self.id: int = Observer._id_counter
        Observer._id_counter += 1

    @abstractmethod
    def update(self, car: Car, msg: str) -> None:
        pass

class CarAppearanceObserver(Observer):
    def update(self, car: Car, msg:str) -> None:
        print(f"Observer {self.id}: {car}: {msg}")
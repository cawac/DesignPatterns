from Cars.Car import Car

class Observer:
    _id_counter: int = 1

    def __init__(self) -> None:
        self.id: int = Observer._id_counter
        Observer._id_counter += 1

    def update(self, car: Car) -> None:
        pass

class CarAppearanceObserver(Observer):
    def update(self, car: Car) -> None:
        print(f"Observer {self.id}: A new car appeared in the container: {car}") 
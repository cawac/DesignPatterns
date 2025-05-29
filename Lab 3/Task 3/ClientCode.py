from Cars.Vehicle import Vehicle
from Cars.Tank import Tank
from Cars.Cargo import Cargo
from Container import Container
from Observer import CarAppearanceObserver

def main() -> None:
    container: Container = Container()
    observer1: CarAppearanceObserver = CarAppearanceObserver()
    observer2: CarAppearanceObserver = CarAppearanceObserver()
    container.add_observer(observer1)
    container.add_observer(observer2)

    car1: Vehicle = Vehicle("Toyota Corolla", 1200, 4.2, 180)
    car2: Tank = Tank("T-34", 26000, 6.7, 55, 76.2, 30, 5)
    car3: Cargo = Cargo("Volvo FH", 8000, 7.5, 120, 18, 900, 3)

    container.add_car(car1)
    container.add_car(car2)
    container.add_car(car3)

if __name__ == "__main__":
    main() 
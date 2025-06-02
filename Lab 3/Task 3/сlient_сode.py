from сars.vehicle import Vehicle, EVehicleClass, EWheelDriveType, EColor
from сars.tank import Tank
from сars.cargo import Cargo
from container import Container
from observer import CarAppearanceObserver

def main() -> None:
    container: Container = Container()
    observer1: CarAppearanceObserver = CarAppearanceObserver()
    observer2: CarAppearanceObserver = CarAppearanceObserver()
    container.add_observer(observer1)
    container.add_observer(observer2)

    car1: Vehicle = Vehicle("Toyota Corolla", 1200, 4.2, 180, EWheelDriveType.ALL, EVehicleClass.COUPE, EColor.RED)
    car2: Tank = Tank("T-34", 26000, 6.7, 55, 76.2, 30, 5)
    car3: Cargo = Cargo("Volvo FH", 8000, 7.5, 120, 18, 900, 3)

    container.add_car(car1)
    container.add_car(car2)
    container.add_car(car3)

    container.update_car(car1, weight=100, max_speed=100, wheel_drive_type=EWheelDriveType.BACK)

if __name__ == "__main__":
    main() 
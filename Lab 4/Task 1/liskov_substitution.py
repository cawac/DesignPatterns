# inherited classes object can correct works after swap with parent class

from abc import abstractmethod

class Car:
    def __init__(self):
        self.driving = False

    @abstractmethod
    def drive(self):
        if self.driving:
            print("already driving")
        else:
            self.driving = True
            print("start driving")

    @abstractmethod
    def stop(self):
        if self.driving:
            self.driving = False
            print("stop driving")
        else:
            print("already stopped")

class BrokenCar(Car):
    def drive(self):
        raise Exception("Engine isn't working")

    def stop(self):
        super().stop()


# right variant

class RightBrokenCar(Car):
    def drive(self):
        pass    # You can call drive method, nothing will happen and nothing break

    def stop(self):
        super().stop()
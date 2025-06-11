# "clients should not be forced to depend upon interfaces that they do not use" - Wikipedia

class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")

# right variant

from abc import ABC, abstractmethod

class RightWorker(ABC):
    @abstractmethod
    def work(self):
        pass

class RightEater(ABC):
    @abstractmethod
    def eat(self):
        pass

class RightRobot(RightWorker):
    def work(self):
        print("Robot working")
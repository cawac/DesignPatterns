from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def sing(self):
        pass

class Dancer(ABC):
    @abstractmethod
    def dance(self):
        pass

class Walker(ABC):
    @abstractmethod
    def walk(self):
        pass

class Inseminator(ABC):
    pass

class EggProducer(ABC):
    @abstractmethod
    def produce_egg(self, partner: Inseminator):
        pass

class EggDefender(ABC):
    @abstractmethod
    def defend_egg(self):
        pass

class SpauseSearcher(ABC):
    @abstractmethod
    def search_for_spause(self):
        pass

class Flying(ABC):
    @abstractmethod
    def fly(self):
        pass
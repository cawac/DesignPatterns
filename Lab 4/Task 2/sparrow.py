from bird_interfaces import *

class Sparrow(Bird, Flying, EggDefender, Dancer, SpauseSearcher, Walker):
    def defend_egg(self):
        print("Hit the enemy")

    def dance(self):
        print("Shake your body")

    def fly(self):
        print("Spread the wings")

    def search_for_spause(self):
        print("Time to search for the spause")
        self.sing()

    def sing(self):
        print("Some Iron Maiden song from 80-th")

    def walk(self):
        print("Walk this way")


class FemaleSparrow(Sparrow, EggProducer):
    def produce_egg(self, partner: Inseminator):
        if partner is Inseminator and partner is Sparrow:
            print("Some magic happens")
        else:
            print("Nothing magic happens")


class MaleSparrow(Sparrow, Inseminator):
    pass
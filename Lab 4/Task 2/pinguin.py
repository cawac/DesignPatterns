from bird_interfaces import *


class Pinguin(Bird, Dancer, Walker, EggDefender, SpauseSearcher):
    def defend_egg(self):
        print('Hit the enemy')

    def dance(self):
        print('Shake your body')

    def search_for_spause(self):
        print("Time to search for the spause")
        self.sing()

    def sing(self):
        print("Some Iron Maiden song from 80-th")

    def walk(self):
        print("Walk this way")


class FemalePinguin(Pinguin, EggProducer):
    def produce_egg(self, partner: Inseminator):
        if partner is Pinguin and partner is Inseminator:
            print("Some magic happens")
        else:
            print("Nothing magic happens")


class MalePinguin(Pinguin, Inseminator):
    pass
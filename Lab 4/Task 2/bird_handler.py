from bird_interfaces import *
from bird_producer import BirdFactory, Sex
from pinguin import FemalePinguin, MalePinguin
from sparrow import FemaleSparrow, MaleSparrow


class BirdHandler:
    def do_bird_action(self):
        male_sparrow: MaleSparrow = BirdFactory.produce_sparrow(Sex.MALE)
        female_sparrow: FemaleSparrow = BirdFactory.produce_sparrow(Sex.FEMALE)

        male_pinguin: MalePinguin = BirdFactory.produce_pinguin(Sex.MALE)
        female_pinguin: FemalePinguin = BirdFactory.produce_pinguin(Sex.FEMALE)

        self.handle_bird_moves(male_sparrow)
        self.handle_bird_moves(male_pinguin)

        self.handle_bird_multiplies(female_sparrow)
        self.handle_bird_multiplies(female_pinguin)

        self.handle_bird_grows_a_child(female_sparrow, male_sparrow)
        self.handle_bird_grows_a_child(female_pinguin, male_pinguin)

    @staticmethod
    def handle_bird_multiplies(bird):
        if bird is SpauseSearcher:
            bird.search_for_spause()
        if bird is Bird:
            bird.sing()
        if bird is Dancer:
            bird.dance()

    @staticmethod
    def handle_bird_moves(bird):
        if bird is Walker:
            bird.walk()
        if bird is Flying:
            bird.fly()

    @staticmethod
    def handle_bird_grows_a_child(bird: EggProducer, bird_partner: Inseminator):
        if bird is EggProducer:
            bird.produce_egg(bird_partner)
        if bird is EggDefender:
            bird.defend_egg()
        if bird_partner is EggDefender:
            bird.defend_egg()
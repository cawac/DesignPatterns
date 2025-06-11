from typing import Optional

from sparrow import *
from pinguin import *
from enum import StrEnum


class Sex(StrEnum):
    MALE = "Male"
    FEMALE = "Female"


class BirdFactory:
    @staticmethod
    def produce_pinguin(sex_of_bird: Sex) -> Optional[Pinguin | MalePinguin | FemalePinguin]:
        if sex_of_bird == Sex.MALE:
            return MalePinguin()
        elif sex_of_bird == Sex.FEMALE:
            return FemalePinguin()
        return None

    @staticmethod
    def produce_sparrow(sex_of_bird: Sex) -> Optional[Sparrow | MaleSparrow | FemaleSparrow]:
        if sex_of_bird == Sex.MALE:
            return MaleSparrow()
        elif sex_of_bird == Sex.FEMALE:
            return FemaleSparrow()
        return None
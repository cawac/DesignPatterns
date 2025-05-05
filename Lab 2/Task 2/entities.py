from dataclasses import dataclass
from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

@dataclass
class SomeEntity:
    id: int
    name: str
    description: str
    status: Status

@dataclass
class SomeImageEntity(SomeEntity):
    image_url: str 
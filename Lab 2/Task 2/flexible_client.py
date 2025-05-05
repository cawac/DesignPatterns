from typing import List
from .entities import SomeEntity, Status
from .api_controller import ApiController

class FlexibleApiClient:
    def __init__(self, api_controller: ApiController):
        self._api = api_controller

    def get_by_filter(self, func: callable) -> List[SomeEntity]:
        return self._api.get_by_filter(func)

    def print(self, entity_id: int) -> str:
        return self._api.print(entity_id)

    def print_many(self, entity_ids: List[int]) -> List[str]:
        return self._api.print_many(entity_ids)

    def set_status(self, entity_id: int, status: Status) -> SomeEntity:
        return self._api.set_status(entity_id, status)

    def deactivate(self, entity_id: int) -> SomeEntity:
        return self._api.deactivate(entity_id)

    def activate(self, entity_id: int) -> SomeEntity:
        return self._api.activate(entity_id) 
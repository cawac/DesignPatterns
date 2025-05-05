from typing import List
from entities import SomeEntity, Status
from api_controller import ApiController

class CrudApiClient:
    def __init__(self, api_controller: ApiController | None):
        self._api: ApiController | None = api_controller
        if api_controller is None:
            self._api = ApiController()

    def create(self, name: str, description: str, status: Status = Status.ACTIVE) -> SomeEntity:
        return self._api.create(name, description, status)

    def update(self, id: int, name: str = None, description: str = None, status: Status = None) -> SomeEntity | None:
        return self._api.update(id, name, description, status)

    def get_one(self, entity_id: int) -> SomeEntity | None:
        return self._api.get_one(entity_id)

    def get_many(self, entity_ids: List[int]) -> List[SomeEntity | None] | None:
        return self._api.get_many(entity_ids)

    def delete(self, entity_id: int) -> bool:
        return self._api.delete(entity_id)

    def delete_many(self, entity_ids: List[int]) -> bool:
        return self._api.delete_many(entity_ids) 
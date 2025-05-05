from typing import List, Optional
from entities import SomeImageEntity, Status
from api_controller import ApiController

class ImageApi:
    def __init__(self, api_controller: ApiController | None):
        self._api: ApiController | None = api_controller
        if api_controller is None:
            self._api = ApiController()

    def get_image(self, entity_id: int) -> str:
        entity = self._api.get_one(entity_id)
        if isinstance(entity, SomeImageEntity):
            return entity.image_url
        else:
            return ""

    def set_image(self, entity_id: int, image_url: str) -> SomeImageEntity | None:
        entity = self._api.get_one(entity_id)

        if entity is None:
            return None
        
        if isinstance(entity, SomeImageEntity):
            entity.image_url=image_url
            return entity
        else:
            image_entity = SomeImageEntity(
                id=entity.id,
                name=entity.name,
                description=entity.description,
                status=entity.status,
                image_url=image_url
            )
            self._api.delete(entity_id)
            self._api.add(image_entity)
            return image_entity


    def get_entities_by_filter(self, filter_func: callable) -> List[SomeImageEntity]:
        return self._api.get_by_filter(filter_func)
from typing import Dict, List, Optional
from entities import SomeEntity, Status


storage: Dict[int, SomeEntity] = dict()


class ApiController:
    def add(self, entity: SomeEntity) -> Optional[SomeEntity]:
        if entity and entity.id not in storage:
            storage[entity.id] = entity
        return None

    def create(self, name: str, description: str, status: Status = Status.ACTIVE) -> SomeEntity:
        entity_id = len(storage) + 1
        entity = SomeEntity(id=entity_id, name=name, description=description, status=status)
        storage[entity_id] = entity
        return entity

    def update(self, id: int, name: str = None, description: str = None, status: Status = None) -> SomeEntity | None:
        entity = self.get_one(id)
        
        if entity is None:
            return None
            
        entity.name = name
        entity.description = description
        entity.status = status            
        return entity

    def get_one(self, entity_id: int) -> SomeEntity | None:
        if entity_id in storage:
            return storage[entity_id]
       
        return None

    def get_many(self, entity_ids: List[int]) -> List[SomeEntity | None] | None:
        return [self.get_one(id) for id in entity_ids if id in storage]

    def get_by_filter(self, filter_func: callable) -> List[SomeEntity]:
        return list(filter(filter_func, storage.values()))

    def delete(self, entity_id: int) -> bool:
        if entity_id in storage:
            del storage[entity_id]
            return True
        
        return False

    def delete_many(self, entity_ids: List[int]) -> bool:
        return all(self.delete(id) for id in entity_ids)

    def print(self, entity_id: int) -> None:
        entity = self.get_one(entity_id)
        
        if entity is not None:
            print(f"Entity: {entity.name}, {entity.description}, {entity.status}")
        
        print("Entity not exists")

    def print_many(self, entity_ids: List[int]) -> None:
        for id in entity_ids:
            self.print(id)

    def set_status(self, entity_id: int, status: Status) -> SomeEntity | None:
        entity = self.get_one(entity_id)
        
        if entity is None:
            return None
        
        entity.status = status
        return entity

    def deactivate(self, entity_id: int) -> SomeEntity | None:
        return self.set_status(entity_id, Status.INACTIVE)

    def activate(self, entity_id: int) -> SomeEntity | None:
        return self.set_status(entity_id, Status.ACTIVE) 
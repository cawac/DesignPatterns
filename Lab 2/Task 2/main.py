from entities import Status
from api_controller import ApiController
from crud_client import CrudApiClient
from image_api import ImageApi


if __name__ == "__main__":
    api_controller = ApiController()
    crud_client = CrudApiClient(api_controller)
    image_api = ImageApi(api_controller)

    entity1 = crud_client.create("First Entity", "Description 1")
    entity2 = crud_client.create("Second Entity", "Description 2", Status.INACTIVE)
    
    print("Created entities:")
    api_controller.print(entity1.id)
    api_controller.print(entity2.id)

    updated_entity = crud_client.update(entity1.id, name="Updated First Entity")
    api_controller.print(entity1.id)

    image_entity = image_api.set_image(entity1.id, "https://example.com/image1.jpg")
    api_controller.print(image_entity.id)

    image_url = image_api.get_image(entity1.id)
    print(f"Retrieved image URL: {image_url}")

    print("\nFiltering entities:")
    name_filter = lambda entity: entity.name == "Updated First Entity"
    filtered_by_name = image_api.get_entities_by_filter(name_filter)
    print("Entities with name 'Updated First Entity':")
    for entity in filtered_by_name:
        print(f"- {entity.name}")

    status_filter = lambda entity: entity.status == Status.INACTIVE
    filtered_by_status = image_api.get_entities_by_filter(status_filter)
    print("\nInactive entities:")
    for entity in filtered_by_status:
        print(f"- {entity.name}")

    complex_filter = lambda entity: (
        entity.name.startswith("Second") and 
        entity.status == Status.INACTIVE
    )
    filtered_complex = image_api.get_entities_by_filter(complex_filter)
    print("\nEntities matching complex filter:")
    for entity in filtered_complex:
        print(f"- {entity.name}")

    deleted = crud_client.delete(entity2.id)
    
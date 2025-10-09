from fastapi import HTTPException


def get_entity_or_raise(service, entity_id: str, entity_name: str):
    entity = service.get_by_id(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail=f"{entity_name} {entity_id} not found")
    return entity

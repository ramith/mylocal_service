from application.api.mylocal.models.entity import Entity
from application.api.mylocal.models.ent_type import EntType

class EntityController:
    def __init__(self, entity_id):
        self.entity = Entity(entity_id)

    def get_entity(entity_id):
        return Entity(entity_id).get_entity()

    def get_entities_ids_by_gnd(gnd_id):
        gnd_entity = Entity(gnd_id).get_entity_ids_by_gnd()
        return {
            EntType.PROVINCE.name : gnd_entity[f'{EntType.PROVINCE.name}_id'],
            EntType.DISTRICT.name : gnd_entity[f'{EntType.DISTRICT.name}_id'],
            EntType.DSD.name : gnd_entity[f'{EntType.DSD.name}_id'],
            EntType.GND.name : gnd_entity[f'{EntType.GND.name}_id']
        }


    def get_entity_ids_by_coordinates(coordinates):
        lat, _, lng = coordinates.partition(',')
        coordinates = [(float)(lat), (float)(lng)]

        gnd_id = Entity(coordinates=coordinates, type='gnd').get_id()
        return EntityController.get_entities_ids_by_gnd(gnd_id)


    def get_entities(entity_ids):
        entity_ids = entity_ids.split(';')
        entity_map = {}
        for entity_id in entity_ids:
            entity_map[entity_id] = Entity(entity_id).get_entity()

        return entity_map

    def get_coordinates(entity_id):
        return {"coordinates": [Entity(entity_id).get_coordinates()], "type":"MultiPolygon"}
    
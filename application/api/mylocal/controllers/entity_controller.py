from application.api.mylocal.models.entity import Entity
from application.api.mylocal.helpers.ent_type import EntType
from application.api.mylocal.models.geo_data import GeoData

class EntityController:
    def __init__(self, entity_id):
        self.entity = Entity(entity_id)

    @classmethod
    def get_entity(cls, entity_id):
        return Entity(entity_id).get_entity()

    @classmethod
    def get_entities_ids_by_gnd(cls, gnd_id):
        gnd_entity = Entity(gnd_id).get_entity_ids_by_gnd()
        return {
            EntType.PROVINCE.name : gnd_entity[f'{EntType.PROVINCE.name}_id'],
            EntType.DISTRICT.name : gnd_entity[f'{EntType.DISTRICT.name}_id'],
            EntType.DSD.name : gnd_entity[f'{EntType.DSD.name}_id'],
            EntType.GND.name : gnd_entity[f'{EntType.GND.name}_id']
        }

    @classmethod
    def get_entity_ids_by_coordinates(cls, coordinates):
        lat, _, lng = coordinates.partition(',')
        coordinates = [(float)(lat), (float)(lng)]

        gnd_id = Entity(coordinates=coordinates, type='gnd').get_id()
        return EntityController.get_entities_ids_by_gnd(gnd_id)

    @classmethod
    def get_entities(cls, entity_ids):
        entity_ids = entity_ids.split(';')
        entity_map = {}
        for entity_id in entity_ids:
            entity_map[entity_id] = Entity(entity_id).get_entity()

        return entity_map
    @classmethod
    def get_coordinates(cls, entity_id):
        return {"coordinates": [Entity(entity_id).get_coordinates()], "type":"MultiPolygon"}
    
    @classmethod
    def get_entity_ids(cls):
        return GeoData(type = 'gnd').get_entity_ids()
    
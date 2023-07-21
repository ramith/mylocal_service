from application.api.mylocal.helpers.ent_type import EntType
from application.api.mylocal.helpers.remote_data import RemoteData
from application.api.mylocal.models.geo_data import GeoData
from application.api.mylocal.helpers.cache import Cache

from shapely.geometry import shape
from ast import literal_eval
from config import ENTS_BASE_URL
from config import CENSUS_BASE_URL

class Entity:
    def __init__(self, entity_id = '', coordinates = None, type = None):
        if entity_id == '':
            self.coordinates = coordinates
            self.type = type
            entity_id = self.get_id_by_coordinates
        self.entity_id = entity_id

    @property
    def id(self):
        return self.entity_id
    
    @property
    def coords(self):
        return self.coordinates

    @property
    def get_entity_type(self):
        return EntType.from_id(self.entity_id)
    
    @property
    def get_ent_remote_data_path(self):
        ent_type = self.get_entity_type.name
        return f'{ENTS_BASE_URL}/ents/{ent_type}.tsv'
    
    @property
    def get_ent_remote_data(self):
        return RemoteData(self.get_ent_remote_data_path, type='tsv').get_data()
    
    @property
    def get_json_geo_remote_data_path(self):
        ent_type = self.get_entity_type.name
        return f'{ENTS_BASE_URL}/geo/json/{ent_type}/{self.entity_id}.json'

    @property
    def get_json_geo_remote_data(self):
        return RemoteData(self.get_json_geo_remote_data_path, type='json').get_data()
    
    @property
    def get_entity_by_id(self):
        data = self.get_ent_remote_data
        for d in data:
            if d['id'] == self.entity_id:
                return d
        return None

    @property
    def get_id_by_coordinates(self):
        coordinates = self.coords
        point = shape({'type': 'Point', 'coordinates': [coordinates[1], coordinates[0]]} )

        processed_geo_data = Cache.get_data_from_cache('processed_geo_data')

        if processed_geo_data == None:
            geo_data = {}
            for id, geo in GeoData(type='gnd').get_geo_data().items():
                geo_data[id] = shape(geo)
            Cache.add_data_to_cache('processed_geo_data', geo_data)
            processed_geo_data = geo_data
            
        for id,multi_polygon in processed_geo_data.items():
            if multi_polygon.contains(point):
                return id
            
        return None
    
    @property
    def get_gnd_ent_remote_data_path(self):
        return f'{CENSUS_BASE_URL}/ents/gnd.tsv'
    
    @property
    def get_gnd_ent_remote_data(self):
        return RemoteData(self.get_gnd_ent_remote_data_path, type='tsv').get_data()

    def get_id(self):
        return self.id

    def get_entity(self):
        entity = self.get_entity_by_id
        for key, value in entity.items():
            try:
                entity[key] = literal_eval(value)
                if entity[key].imag > 0 :
                    entity[key] = str(value)
            except:
                pass
            
        return entity  

    def get_entity_ids_by_gnd(self):
        data = self.get_gnd_ent_remote_data
        for d in data:
            if d['id'] == self.id:
                return d
        return None

    def get_coordinates(self):
        return self.get_json_geo_remote_data
    
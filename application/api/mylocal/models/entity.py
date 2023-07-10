from application.api.mylocal.models.ent_type import EntType
from application.api.mylocal.models.remote_data import RemoteData
from shapely.geometry import mapping, Point, shape
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
    def get_topojson_geo_remote_data_path(self):
        ent_type = self.type
        return f'{ENTS_BASE_URL}/geo/topo-geo_json/{ent_type}.topojson'

    @property
    def get_topojson_geo_remote_data(self):
        return RemoteData(self.get_topojson_geo_remote_data_path, type='json').get_data()

    @property
    def get_geo(self):
        geo_data = self.get_topojson_geo_remote_data
        region_to_geo = {}
        for geometry in geo_data['objects']['data']['geometries']:
            coordinates = []
            region_id = geometry['properties']['id']

            for arc in geometry['arcs']:
                arc = arc.pop().pop()
                coordinates.append(geo_data['arcs'][arc])

            region_to_geo[region_id] = {'type': 'multipolygon', 'coordinates': [coordinates]}
        
        return region_to_geo

    @property
    def get_id_by_coordinates(self):
        coordinates = self.coords
        point = shape({'type': 'Point', 'coordinates': [coordinates[1], coordinates[0]]} )

        geo_data = self.get_geo
        for id in geo_data:
            geo = geo_data[id]

            multi_polygon = shape(geo)
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
                entity[key] = eval(value)
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
    
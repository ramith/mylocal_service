from config import ENTS_BASE_URL
from application.api.mylocal.helpers.remote_data import RemoteData
from shapely.geometry import mapping

class GeoData():
    def __init__(self, type):
        self.type = type

    @property
    def __remote_data_path(self):
        ent_type = self.type
        return f'{ENTS_BASE_URL}/geo/topo-geo_json/{ent_type}.topojson'

    @property
    def __remote_data(self):
        return RemoteData(self.__remote_data_path, type='topojson').get_data()

    @property
    def __geo(self):
        geo_data = self.__remote_data
        n_regions = len(geo_data['geometry'])
        region_to_geo = {}
        for i in range(0, n_regions):
            region_id = geo_data['id'][i]
            region_to_geo[region_id] = mapping(geo_data['geometry'][i])
        return region_to_geo

    def get_geo_data(self):
        return self.__geo
    
    def get_entity_ids(self):
        return list(self.__geo.keys())

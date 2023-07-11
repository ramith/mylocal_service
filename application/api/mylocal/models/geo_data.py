from config import ENTS_BASE_URL
from application.api.mylocal.models.remote_data import RemoteData

class GeoData():
    data = None

    def __init__(self, type):
        self.type = type

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

    def get_geo_data(self):
        if GeoData.data is None:
            GeoData.data = self.get_geo
        return GeoData.data

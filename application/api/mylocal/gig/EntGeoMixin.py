import os
import tempfile
import requests

from utils import WWW, JSONFile
from config import GEO_SERVER_URL

class EntGeoMixin:
    @property
    def raw_geo_file(self):
        raw_geo_path = os.path.join(
            tempfile.gettempdir(), f'ent.{self.id}.raw_geo.json'
        )

        return JSONFile(raw_geo_path)

    def get_data(url_remote_geo_data_path: str):
        response = requests.get(url_remote_geo_data_path)
        if response.status_code == 200:
            data = response.json()
        else:
            print('API request failed with status code:', response.status_code)
            data = None
        return data

    def url_remote_geo_data_path(self, endpoint: str):
        id = self.id
        return f'{GEO_SERVER_URL}/{endpoint}/{id}'
    
    def url_remote_geo_data_path(attribute, endpoint: str):
        return f'{GEO_SERVER_URL}/{endpoint}/{attribute}'

    def get_raw_geo(self):
        raw_geo_file = self.raw_geo_file
        if raw_geo_file.exists:
            raw_geo = raw_geo_file.read()
        else:
            raw_geo = WWW(self.url_remote_geo_data_path).readJSON()
            raw_geo_file.write(raw_geo)
        return raw_geo

    def geo(region_id):
        return EntGeoMixin.get_data(EntGeoMixin.url_remote_geo_data_path(attribute = region_id,endpoint='region_geo'))
    
    def latlng_to_region(latlng_str):
        return EntGeoMixin.get_data(EntGeoMixin.url_remote_geo_data_path(attribute =latlng_str , endpoint='latlng_to_region'))
    

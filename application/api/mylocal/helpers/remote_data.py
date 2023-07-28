from utils import WWW
from functools import cached_property
import geopandas
from application.api.mylocal.helpers.cache import Cache
from config import ENTS_BASE_URL, CENSUS_BASE_URL

class RemoteData:
    def __init__(self, url,type):
        self.url = url
        self.type = type

    @cached_property
    def data(self):
        if self.type == 'tsv':
            return WWW(self.url).readTSV()
        if self.type == 'json':
            return WWW(self.url).readJSON()
        if self.type == 'topojson':
            return geopandas.read_file(WWW(self.url).download())

    def get_data(self):
        key = self.url.replace(ENTS_BASE_URL, '').replace(CENSUS_BASE_URL, '')

        if '/geo/json/' in key or 'topojson' in key :
            return self.data
        
        data = Cache.get_data_from_cache(key)
        if data is None:
            data = self.data
            Cache.add_data_to_cache(key, data)
        return data
    
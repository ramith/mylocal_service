from utils import WWW
from functools import cached_property
from application.api.mylocal.helpers.cache import Cache


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
    
    def get_data(self):
        data = Cache.get_data_from_cache(self.url)
        if data is None:
            data = self.data
            Cache.add_data_to_cache(self.url, data)
        return data
    
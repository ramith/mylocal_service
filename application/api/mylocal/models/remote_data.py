from utils import WWW
from functools import cached_property

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
        return self.data
    
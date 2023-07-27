from config import CENSUS_BASE_URL
from application.api.mylocal.helpers.remote_data import RemoteData

class Table:
    def __init__(self, table_name):
        self.table_name = table_name
    
    @property
    def __remote_data_path(self):
        return f'{CENSUS_BASE_URL}/gig2/{self.table_name}.tsv'
    
    @property
    def __remote_data(self):
        return RemoteData(self.__remote_data_path, type='tsv').get_data()
    
    def get_table(self):
        return self.__remote_data
    
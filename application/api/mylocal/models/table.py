from config import CENSUS_BASE_URL
from application.api.mylocal.models.remote_data import RemoteData

class Table:
    def __init__(self, table_name):
        self.table_name = table_name

    def get_table_name(self):
        return self.table_name
    
    @property
    def get_remote_data_path(self):
        return f'{CENSUS_BASE_URL}/gig2/{self.get_table_name()}.tsv'
    
    @property
    def get_remote_data(self):
        return RemoteData(self.get_remote_data_path, type='tsv').get_data()
    
    def get_table(self):
        return self.get_remote_data
    
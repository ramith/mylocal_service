from dataclasses import dataclass
from functools import cached_property

from utils import WWW, FiledVariable

from config import CENSUS_BASE_URL
from application.api.mylocal.gig.GIGTableRow import GIGTableRow

ID_FIELD = 'entity_id'


@dataclass
class GIGTable:
    measurement: str
    ent_type_group: str
    time_group: str

    @property
    def table_id(self):
        return '.'.join(
            [
                self.measurement,
                self.ent_type_group,
                self.time_group,
            ]
        )

    @property
    def url_remote_data_path(self):
        return f'{CENSUS_BASE_URL}/{self.table_id}.tsv'

    @cached_property
    def remote_data_list(self) -> list:
        def inner():
            d_list = WWW(self.url_remote_data_path).readTSV()
            non_null_d_list = [d for d in d_list if d]
            return non_null_d_list

        return FiledVariable(self.table_id + '.remote_data_list', inner).value

    @cached_property
    def remote_data_idx(self) -> dict:
        return {d[ID_FIELD]: d for d in self.remote_data_list}

    def get(self, id):
        return GIGTableRow(self.remote_data_idx[id])


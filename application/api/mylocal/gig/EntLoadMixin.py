import json

from rapidfuzz import fuzz
from utils import String

from application.api.mylocal.gig.EntType import EntType


class EntLoadMixin:
    @classmethod
    def from_dict(cls, d):
        d = d.copy()

        for k in ['area', 'population', 'centroid_altitude']:
            if k in d:
                d[k] = String(d[k]).int if d[k] else 0

        for k in ['centroid', 'subs', 'supers', 'ints', 'eqs']:
            if k in d and d[k]:
                d[k] = json.loads(d[k].replace('\'', '"'))
        return cls(d)

    @classmethod
    def from_id(cls, id: str):
        ent_type = EntType.from_id(id)
        ent_idx = cls.idx_from_type(ent_type)
        return ent_idx[id]

    @classmethod
    def list_from_type(cls, ent_type: EntType) -> list:
        d_list = ent_type.remote_data_list
        ent_list = [cls.from_dict(d) for d in d_list]
        return ent_list

    @classmethod
    def idx_from_type(cls, ent_type: EntType) -> dict:
        ent_list = cls.list_from_type(ent_type)
        ent_idx = {ent.id: ent for ent in ent_list}
        return ent_idx

    @classmethod
    def list_from_id_list(cls, id_list: list) -> list:
        ent_list = [cls.from_id(id) for id in id_list]
        return ent_list

    @classmethod
    def ids_from_type(cls, ent_type: EntType) -> list:
        ent_list = cls.list_from_type(ent_type)
        id_list = [ent.id for ent in ent_list]
        return id_list

    @classmethod
    def list_from_name_fuzzy(
        cls,
        name_fuzzy: str,
        filter_ent_type: EntType = None,
        filter_parent_id: str = None,
        limit: int = 5,
        min_fuzz_ratio: int = 80,
    ) -> list:
        entity_type_list = (
            [filter_ent_type] if filter_ent_type else EntType.list()
        )

        ent_and_ratio_list = []
        for entity_type in entity_type_list:
            for ent in cls.list_from_type(entity_type):
                if filter_parent_id and not ent.is_parent_id(
                    filter_parent_id
                ):
                    continue

                fuzz_ratio = fuzz.ratio(ent.name, name_fuzzy)
                ent_and_ratio_list.append([ent, fuzz_ratio])

        return [
            item[0]
            for item in sorted(ent_and_ratio_list, key=lambda x: -x[1])
            if item[1] >= min_fuzz_ratio
        ][:limit]

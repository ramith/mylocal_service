import json


class EntJSONMixin:
    def to_json(self):
        return json.dumps(self.d)

    @classmethod
    def from_json(cls, json_str):
        d = json.loads(json_str)
        return cls(d)

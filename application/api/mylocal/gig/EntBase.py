class EntBase:
    def __init__(self, d):
        self.d = d

    @property
    def id(self):
        return self.d["id"]

    @property
    def name(self):
        return self.d["name"]

    @property
    def acronym(self):
        return "".join([c for c in self.name if c.isupper()])

    @property
    def short_name(self):
        # remove lowecase vowels
        return (
            "".join([c for c in self.name if c not in "aeiou"])
            .replace('.', '')
            .replace('-', '')
        )

    @property
    def lnglat(self):
        centroid = self.d["centroid"]
        return [centroid[1], centroid[0]]

    def is_parent_id(self, cand_parent_id: str):
        return cand_parent_id in self.id

    def __getattr__(self, key: str):
        if key in self.d.keys():
            return self.d.get(key)
        raise AttributeError

    def __str__(self):
        return str(self.d)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, EntBase):
            return self.d == other.d
        return False

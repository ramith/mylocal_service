class Cache:
    cache = {}

    def __init__(self):
        pass

    @classmethod
    def get_data_from_cache(cls, key):
     return Cache.cache.get(key, None)

    @classmethod
    def add_data_to_cache(cls, key, data):
        Cache.cache[key] = data
        return True
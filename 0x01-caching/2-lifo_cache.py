#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching algorithme"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """
        put item in cash storage with a key
        """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                try:
                    beforelastkey = list(self.cache_data.keys())[-2]
                except IndexError:
                    beforelastkey = None
                if beforelastkey is not None:
                    del self.cache_data[beforelastkey]
                print(f'DISCARD: {beforelastkey}')

    def get(self, key):
        """get the item from cache by key"""
        return self.cache_data.get(key, None)

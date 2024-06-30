#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching algorithme"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(reversed(self.cache_data))[1]
                del self.cache_data[last_key]
                print(f'DISCARD: {last_key}')

    def get(self, key):
        """get the item from cache by key"""
        return self.cache_data.get(key, None)

#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get item from the cache by a key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

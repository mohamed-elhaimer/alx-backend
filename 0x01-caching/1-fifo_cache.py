#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache Algorithme"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """put in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')

    def get(self, key):
        """get item from cache by key"""
        return self.cache_data.get(key)

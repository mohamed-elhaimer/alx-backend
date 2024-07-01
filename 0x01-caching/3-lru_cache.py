#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching Algorithme"""
    def __init__(self):
        """constructor"""
        super().__init__()
        self.history = []

    def put(self, key, item):
        """put item in cash storage with a key"""
        if key and item:
            if key in self.history:
                self.history.remove(key)
            elif (len(self.cache_data)) >= BaseCaching.MAX_ITEMS:
                lru_key = self.history.pop(0)
                del self.cache_data[lru_key]
                print(f'DISCARD: {lru_key}')
            self.cache_data[key] = item
            self.history.append(key)

    def get(self, key):
        """get the item from cache by key"""
        if key in self.cache_data:
            self.history.remove(key)
            self.history.append(key)
        return self.cache_data.get(key, None)

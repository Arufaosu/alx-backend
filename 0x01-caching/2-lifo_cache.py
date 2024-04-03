#!/usr/bin/python3
"""2-lifo_cache.py"""
from base_caching import BaseCaching
from collections import deque

class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """initializes caching system"""
        super().__init__()
        self.last_in_keys = deque()

    def put(self, key, item):
        """adds an item in the cache"""
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.last_in_keys.popleft()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            self.cache_data[key] = item

            if key in self.last_in_keys:
                self.last_in_keys.remove(key)

            self.last_in_keys.appendleft(key)

    def get(self, key):
        """gets an item by key"""
        return self.cache_data.get(key)

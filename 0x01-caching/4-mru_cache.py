#!/usr/bin/python3
"""4-mru_cache.py"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """initializes the caching system"""
        super().__init__()
        self.lru_keys = deque()

    def put(self, key, item):
        """adds an item in the cache"""
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.lru_keys.pop()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            self.cache_data[key] = item

            if key in self.lru_keys:
                self.lru_keys.remove(key)

            self.lru_keys.appendleft(key)

    def get(self, key):
        """gets an item by key"""
        item = self.cache_data.get(key)

        if item:
            if key in self.lru_keys:
                self.lru_keys.remove(key)

            self.lru_keys.appendleft(key)

        return item

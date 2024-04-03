#!/usr/bin/env python3
"""MRUCache: Cache with Most Recently Used algorithm
"""
from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """MRU caching system
    """

    def __init__(self):
        """Initialize the caching system
        """
        super().__init__()
        self.mru_keys = deque()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.mru_keys.popleft()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

            self.cache_data[key] = item

            if key in self.mru_keys:
                self.mru_keys.remove(key)

            self.mru_keys.appendleft(key)

    def get(self, key):
        """Get an item by key
        """
        item = self.cache_data.get(key)

        if item:
            if key in self.mru_keys:
                self.mru_keys.remove(key)

            self.mru_keys.appendleft(key)

        return item

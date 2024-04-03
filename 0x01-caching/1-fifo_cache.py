#!/usr/bin/python3
"""1-fifo_cache.py"""
from base_caching import BaseCaching
from collections import deque

class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.first_in_keys = deque()

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                key_to_remove = self.first_in_keys.pop()
                self.cache_data.pop(key_to_remove)
                print('DISCARD:', key_to_remove)

                self.cache_data[key] = item

                if key in self.first_in_keys:
                    self.first_in_keys.remove(key)

                self.first_in_keys.appendleft(key)
        
        def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key)

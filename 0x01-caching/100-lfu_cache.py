#!/usr/bin/python3
"""100-lfu_cache.py"""
from base_caching import BaseCaching
from collections import deque


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """initializes the caching system"""
        super().__init__()

        self.lfu_keys = {}

        self.lru_keys = deque()

    def put(self, key, item):
        """adds an item in the cache"""
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                min_uses = min(self.lfu_keys.values())

                least_fu_keys = [key for key, n_uses in self.lfu_keys.items()
                                 if n_uses == min_uses]

                for idx in range(len(self.lru_keys) - 1, -1, -1):
                    if self.lru_keys[idx] in least_fu_keys:
                        key_to_remove = self.lru_keys[idx]
                        self.lru_keys.remove(key_to_remove)
                        self.lfu_keys.pop(key_to_remove)
                        self.cache_data.pop(key_to_remove)
                        print('DISCARD:', key_to_remove)
                        break

            self.cache_data[key] = item
            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

            if key in self.lru_keys:
                self.lru_keys.remove(key)

            self.lru_keys.appendleft(key)

    def get(self, key):
        """gets an item by key"""
        item = self.cache_data.get(key)

        if item:

            self.lfu_keys[key] = self.lfu_keys.get(key, 0) + 1

            if key in self.lru_keys:
                self.lru_keys.remove(key)

            self.lru_keys.appendleft(key)

        return item

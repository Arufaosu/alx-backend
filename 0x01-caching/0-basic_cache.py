#!/usr/bin/python3
"""0-basic_cache.py"""
BasicCache = __import__('0-basic_cache').BasicCache

class BasicCache(BaseCaching):
    """defines a basic caching system"""

    def put(self, key, item):
        """adds an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None


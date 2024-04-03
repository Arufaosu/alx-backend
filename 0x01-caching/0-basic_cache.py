#!/usr/bin/python3
"""0-basic_cache.py"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """defines a basic caching system"""

    def put(self, key, item):
        """adds an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves an item from the cache"""
        return self.cache_data.get(key)
        

#!/usr/bin/env python3
""" Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    """
    def put(self, key, item):
        """ assigns the new item to the dictionary
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]

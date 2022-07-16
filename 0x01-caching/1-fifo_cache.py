#!/usr/bin/env python3
""" FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ assigns the new item to the dictionary
        """
        if not (key is None or item is None):
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_in = list(self.cache_data.keys())[0]
                del self.cache_data[first_in]
                print(f'DISCARD: {first_in}')

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]

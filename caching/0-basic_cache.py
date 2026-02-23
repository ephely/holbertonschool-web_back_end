#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache """
    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data
        linked to key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

#!/usr/bin/env python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data
        linked to key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)

#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in
        self.cache_data linked to key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

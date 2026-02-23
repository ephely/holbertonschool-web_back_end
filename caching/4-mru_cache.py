#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache """

    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data
        linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
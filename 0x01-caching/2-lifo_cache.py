#!/usr/bin/env python3
"""this module contain class FIFOCache"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    this class for least in first out cache
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """this method to put value in cache"""

        if key is None or item is None:
            return
        if self.cache_data.get(key, None) is not None:
            self.cache_data[key] = item
        else:
          if len(self.stack) == self.MAX_ITEMS:
              poped_key = self.stack.pop()
              self.cache_data.pop(poped_key)
              print("DISCARD: {}".format(poped_key))
          self.stack.append(key)
          self.cache_data[key] = item


    def get(self, key):
        """this method to get value from cache"""
        return self.cache_data.get(key, None)

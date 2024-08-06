#!/usr/bin/env python3
"""this module contain class FIFOCache"""

from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """
    this class for first in first out cache
    """

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """this method to put value in cache"""

        if key is None or item is None:
            return
        if self.cache_data.get(key, None) is None:
            self.queue.append(key)
        self.cache_data[key] = item
        if len(self.queue) > self.MAX_ITEMS:
            poped_key = self.queue.popleft()
            self.cache_data.pop(poped_key)
            print("DISCARD: {}".format(poped_key))

    def get(self, key):
        """this method to get value from cache"""
        return self.cache_data.get(key, None)

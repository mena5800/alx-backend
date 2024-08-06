#!/usr/bin/env python3
"""this module contain class BasicCache"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
  """
  this class for base cache
  """
  def __init__(self):
    super().__init__()
  
  def put(self, key, item):
    """this method to put value in cache"""
    if key is None or item is None:
      return
    self.cache_data[key] = item
  
  def get(self, key):
    """this method to get value from cache"""
    return self.cache_data.get(key, None) 
#!/usr/bin/env python3
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
  def __init__(self):
    super().__init__()
  
  def put(self, key, item):
    self.cache_data[key]

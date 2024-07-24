#!/usr/bin/env python3
"""
Defines a MRU cache class.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """An MRU cache."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """Add an item to the cache."""
        if key is None or value is None:
            return

        if key not in self.cache_data.keys() and \
                len(self.cache_data) >= self.MAX_ITEMS:
            # Delete the oldest data based on access time.
            k, _ = self.cache_data.popitem(last=True)
            # Print the discarded kay
            print("DISCARD:", k)

        # Move the data to the end of the cache
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)

        self.cache_data[key] = value

    def get(self, key):
        """Get an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.cache_data.move_to_end(key)
        return value

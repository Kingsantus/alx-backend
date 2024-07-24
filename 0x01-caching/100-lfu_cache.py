#!/usr/bin/env python3
"""
Defines a LRFU cache class.
"""

from base_caching import BaseCaching
from collections import OrderedDict
from time import time


class LFUCache(BaseCaching):
    """An LRFU cache."""

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
            # Delete the oldest least frequently used item
            k = self.pop_lfru_item()
            # Print the discarded kay
            print("DISCARD:", k)

        if key not in self.cache_data:
            self.cache_data[key] = {'freq': 0}

        self.cache_data[key]['value'] = value
        self.cache_data[key]['freq'] += 1
        self.cache_data[key]['last_accessed'] = time()

    def get(self, key):
        """Get an item from the cache."""
        item = self.cache_data.get(key, None)
        if item:
            item['last_accessed'] = time()
            item['freq'] += 1
            return item['value']
        else:
            return None

    def pop_lfru_item(self):
        """Remove the least frequent and leastly recently used item."""
        # Sort items firt based on frequency, then based on access time
        sorted_items = sorted(
            self.cache_data.items(),
            key=(
                lambda item: (item[1]['freq'],
                              item[1]['last_accessed'])
                )
        )
        # Pop the LFRU item and return the key
        lfru_key = sorted_items[0][0]
        self.cache_data.pop(lfru_key)
        return lfru_key

    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)['value']))

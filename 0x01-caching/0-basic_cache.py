#!/usr/bin/env python3
"""
Implement a basic cache class that stores an unlimited number of items
to an in-memory dictionary.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache for storing items to an in-memory dict."""
    MAX_ITEMS = None

    def put(self, key, item):
        """Add an item to the cache using the specified key."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache using the specified key."""
        return self.cache_data.get(key, None)

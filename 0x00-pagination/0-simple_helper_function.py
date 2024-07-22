#!/usr/bin/env python3
"""
index_range function return a tuple
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """
    index_range calulate the start index and end index for pagination.

    Args:
        page: the number of page
        page_size: the number of items per page.

    Returns:
        tuple: containing the start and end index.
    """
    return ((page-1) * page_size, page_size * page)

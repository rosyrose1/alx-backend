#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): Page number to return (pages are 1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing start_index and end_index.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)

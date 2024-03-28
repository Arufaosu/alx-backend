#!/usr/bin/env python3
"""0-simple_helper_function.py"""

def index_range(page, page_size):
    """calculate the start and end indexes"""
    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index

if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)

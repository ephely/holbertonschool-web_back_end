#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer
arguments page and page_size.
"""

import csv
from typing import List, Dict, Optional
import math


def index_range(page: int, page_size: int) -> tuple:
    "Return a tuple of start and end indexes for pagination."
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end] if start < len(data) else []
        
    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Optional[object]]:
        """
        Retrieve a page of the dataset with hypermedia pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """find the correct indexes to paginate the dataset correctly"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        self.dataset()
        if end_index > len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            Hypermedia pagination
        """
        hypermedia = {}
        data = self.get_page(page, page_size)
        hypermedia['page_size'] = page_size
        hypermedia['page'] = page
        hypermedia['data'] = data
        next_start, next_end = index_range(page + 1, page_size)
        if next_end <= len(self.__dataset):
            hypermedia['next_page'] = page + 1
        else:
            hypermedia['next_page'] = None
        if page > 1:
            hypermedia['prev_page'] = page - 1
        else:
            hypermedia['prev_page'] = None
        hypermedia['total_pages'] = math.ceil(len(self.__dataset) / page_size)
        return hypermedia

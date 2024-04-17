from inventory_report.product import Product
from typing import List, Optional


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None) -> None:
        if data is None:
            data = []

        self._data = data

    @property
    def data(self):
        return self._data.copy()

    def add_data(self, data: List[Product]):
        self._data.extend(data)

from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import List


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        return ()


class JsonImporter:
    pass


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

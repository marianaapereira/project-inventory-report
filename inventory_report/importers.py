from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import List
import json


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        return ()


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, 'r') as json_file:
            data_list = json.load(json_file)

        product_list = []

        for data in data_list:
            new_product = Product(
                data["id"],
                data["product_name"],
                data["company_name"],
                data["manufacturing_date"],
                data["expiration_date"],
                data["serial_number"],
                data["storage_instructions"]
            )

            product_list.append(new_product)

        return product_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

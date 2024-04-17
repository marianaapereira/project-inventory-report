from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import List
import json
import csv


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        ...


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


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            data_list = list(csv_reader)

            product_list = []

            for data in data_list:
                new_product = Product(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6]
                )

                product_list.append(new_product)

            return product_list


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

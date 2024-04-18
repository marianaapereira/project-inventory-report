from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report
from datetime import datetime


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def get_oldest_manufacturing_date(self):
        current_date = datetime.today()
        oldest_manufacturing_date = current_date
        date_format = "%Y-%m-%d"

        for inventory in self.inventories:
            for product in inventory.data:
                product_manufacturing_date = datetime.strptime(
                    product.manufacturing_date,
                    date_format
                )

                if ((current_date - oldest_manufacturing_date)
                        < (current_date - product_manufacturing_date)):
                    oldest_manufacturing_date = product_manufacturing_date

        return oldest_manufacturing_date.strftime(date_format)

    def get_closest_expiration_date(self):
        current_date = datetime.today()
        closest_expiration_date = None
        date_format = "%Y-%m-%d"

        for inventory in self.inventories:
            for product in inventory.data:
                product_expiration_date = datetime.strptime(
                    product.expiration_date,
                    date_format
                )

                if (product_expiration_date > current_date):
                    if (
                        closest_expiration_date is None
                        or (product_expiration_date - current_date)
                        < (closest_expiration_date - current_date)
                    ):
                        closest_expiration_date = product_expiration_date

        return closest_expiration_date.strftime(date_format)

    def get_companies_inventories(self):
        companies_names = list(set(
            product.company_name
            for inventory in self.inventories
            for product in inventory.data
        ))
        companies_inventories = []

        for company in companies_names:
            company_product_counter = 0

            for inventory in self.inventories:
                for product in inventory.data:
                    if product.company_name == company:
                        company_product_counter += 1

            companies_inventories.append((company, company_product_counter))

        sorted_companies_inventories = sorted(
            companies_inventories,
            key=lambda company: company[1],
            reverse=True
        )

        return sorted_companies_inventories

    def generate(self) -> str:
        oldest_manufacturing_date = self.get_oldest_manufacturing_date()
        closest_expiration_date = self.get_closest_expiration_date()
        companies_inventories = self.get_companies_inventories()
        company_largest_inventory = companies_inventories[0][0]

        return (
            "Oldest manufacturing date: "
            f"{oldest_manufacturing_date}\n"
            "Closest expiration date: "
            f"{closest_expiration_date}\n"
            "Company with the largest inventory: "
            f"{company_largest_inventory}\n"
        )

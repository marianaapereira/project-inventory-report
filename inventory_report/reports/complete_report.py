from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        simple_report = super().generate()
        companies_inventories = super().get_companies_inventories()
        output_lines = []

        for company in companies_inventories:
            output_lines.append(f"- {company[0]}: {company[1]}\n")

        output_lines = "".join(output_lines)

        return (
            f"{simple_report}"
            "Stocked products by company:\n"
            f"{output_lines}"
        )

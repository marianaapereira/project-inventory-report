from inventory_report.product import Product


def test_product_report() -> None:
    example_product = {
        "id": "0000",
        "product_name": "Ice",
        "company_name": "Trybe - TR",
        "manufacturing_date": "2024-04-17",
        "expiration_date": "2025-04-17",
        "serial_number": "FL20 D4XM 4815 45HP 9263 MNZQ 3H5K",
        "storage_instructions": "Store in the fridge"
    }

    new_product = Product(
        example_product["id"],
        example_product["product_name"],
        example_product["company_name"],
        example_product["manufacturing_date"],
        example_product["expiration_date"],
        example_product["serial_number"],
        example_product["storage_instructions"]
    )

    expected_response = (
        "The product 0000 - Ice "
        "with serial number FL20 D4XM 4815 45HP 9263 MNZQ 3H5K "
        "manufactured on 2024-04-17 "
        "by the company Trybe - TR "
        "valid until 2025-04-17 "
        "must be stored according to the following instructions: "
        "Store in the fridge."
    )

    str_response = new_product.__str__()
    assert str_response == expected_response

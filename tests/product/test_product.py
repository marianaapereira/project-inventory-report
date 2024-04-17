from inventory_report.product import Product


def test_create_product() -> None:
    example_product = {
        "id": "0000",
        "product_name": "Ice",
        "company_name": "Trybe - TR",
        "manufacturing_date": "2024-04-17",
        "expiration_date": "2099-04-17",
        "serial_number": "FL20 D4XM 4815 45HP 9263 MNZQ 3H5K",
        "storage_instructions": "Store in the fridge."
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

    assert new_product.id == example_product["id"]
    assert new_product.product_name == example_product["product_name"]
    assert new_product.company_name == example_product["company_name"]
    assert (
        new_product.manufacturing_date == example_product["manufacturing_date"]
    )
    assert new_product.expiration_date == example_product["expiration_date"]
    assert new_product.serial_number == example_product["serial_number"]
    assert (
        new_product.storage_instructions
        == example_product["storage_instructions"]
    )

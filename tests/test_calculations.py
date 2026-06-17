import pytest
from src.utils.calculations import calculate_total
from src.models.product import Product

def test_calculate_total():

    PRODUCT_1 = Product("Laptop", "123456789012", 100.00, 10, "Electronics")
    PRODUCT_2 = Product("Notebook", "987654321098", 2.50, 150, "Office Supplies")
    PRODUCT_3 = Product("Water Bottle", "555666777888", 13.00, 35, "Sports")
    PRODUCT_4 = Product("Coffee Mug", "111222333444", 7.00, 0, "Kitchen")

    cart = [PRODUCT_1, PRODUCT_2, PRODUCT_3, PRODUCT_4]

    total = {"value": 0.0}
    for item in cart:
        calculate_total(total= total, item= item)

    assert total["value"] == 122.5


"""
Manual testing for functions
"""

from src.services.spreadsheet import add_row,delete_row
from src.models.product import Product

def test_add_row():
    product2 = Product(
        barcode="7501000123456",
        name="Pan Bimbo",
        price=35.00,
        quantity=5,
        category="Panadería"
    )

    product3 = Product(
        barcode="7501000654321",
        name="Coca Cola 600ml",
        price=22.00,
        quantity=10,
        category="Bebidas"
    )

    add_row(product2)
    add_row(product3)

def test_delete_row():
    column = "Nombre"
    info = "Pan Bimbo"

    delete_row(column, info)

if __name__ == "__main__":
    test_delete_row()
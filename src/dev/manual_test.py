"""
Manual testing for functions
"""

from src.services.spreadsheet import add_row,delete_row,read_rows
from src.models.product import Product
from src.utils.mappers import df_to_Product
from src.services.check_sys import check_system

def test_add_row():
    product3 = Product(
        barcode="7501000123456",
        name="Pan Bimbo",
        price=35.00,
        quantity=5,
        category="Panadería"
    )

    product4 = Product(
        barcode="7501000987654",
        name="Leche Lala 1L",
        price=28.50,
        quantity=8,
        category="Lácteos"
    )

    product5 = Product(
        barcode="7501000112233",
        name="Huevos 12 piezas",
        price=42.00,
        quantity=12,
        category="Abarrotes"
    )

    product6 = Product(
        barcode="7501000445566",
        name="Arroz 1kg",
        price=25.00,
        quantity=20,
        category="Granos"
    )

    product7 = Product(
        barcode="7501000778899",
        name="Frijoles 1kg",
        price=30.00,
        quantity=15,
        category="Granos"
    )

    product8 = Product(
        barcode="7501000123987",
        name="Sabritas Original 45g",
        price=18.00,
        quantity=25,
        category="Botanas"
    )

    product9 = Product(
        barcode="7501000654789",
        name="Agua Bonafont 1.5L",
        price=15.00,
        quantity=30,
        category="Bebidas"
    )

    product10 = Product(
        barcode="7501000321654",
        name="Jabón Zote",
        price=12.00,
        quantity=18,
        category="Limpieza"
    )

    add_row(product3)
    add_row(product4)
    add_row(product5)
    add_row(product6)
    add_row(product7)
    add_row(product8)
    add_row(product9)
    add_row(product10)

def test_delete_row():
    column = "Nombre"
    info = "Pan Bimbo"

    delete_row(column, info)

def test_df_to_Product():
    column = "SKU"
    data = 7501000112233
    df = read_rows(column, data)

    product_obj= df_to_Product(df, Product)
    print(type(product_obj))


if __name__ == "__main__":
    check_system()
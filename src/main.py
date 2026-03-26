from itertools import product

from models.product import Product
from services.spreadsheet import add_row, create_spreasdsheet

def debug():
    product1 = Product(
        barcode="7501031311309",
        name="Leche 1L",
        price=25.50,
        quantity=2,
        category="Lácteos"
    )

    create_spreasdsheet()
    add_row(product1)


def main():
    debug()


if __name__ == "__main__":
    main()
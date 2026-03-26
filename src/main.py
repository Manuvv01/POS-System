from models.product import Product
from services.spreadsheet import add_row

def debug():
    product1 = Product(
        barcode="7501031311309",
        name="Leche 1L",
        price=25.50,
        quantity=2,
        category="Lácteos"
    )

    


def main():
    debug()


if __name__ == "__main__":
    main()
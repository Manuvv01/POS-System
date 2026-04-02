"""
Displays the values shown to the app.py
"""
from src.services.spreadsheet import read_rows
from src.utils.mappers import df_to_Product
from src.models.product import Product

def display_scannedItem(column, data):
    """
    Display the item to appear in the display at checking

    :param:
        column (str): String that shows the column of the file
        data (int): data of the product by SKU

    """
    NAME_WIDTH = 30
    PRICE_WIDTH = 8
    df = read_rows(column, data)

    product_obj= df_to_Product(df,Product)
    product_str = f"{product_obj.name:<{NAME_WIDTH}} ${product_obj.price:>{PRICE_WIDTH}.2f}"
    return product_str
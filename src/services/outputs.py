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
    df = read_rows(column, data)

    product_obj= df_to_Product(df,Product)
    product_str= f"{product_obj.name}    ${product_obj.price}"
    return product_str
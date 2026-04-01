"""
Displays the values shown to the app.py
"""
from src.services.spreadsheet import read_rows
from src.utils.mappers import df_to_Product
from src.models.product import Product

def display_scannedItem(column, data):
    df = read_rows(column, data)

    product_obj= df_to_Product(df,Product)
    product_str= f"{product_obj.name}    ${product_obj.price}"
    return product_str
"""
Haandles conversion between DataFrame rows and Product objects
"""
import pandas
from ..models.product import Product
from src.models.cart import Cart
from src.services.spreadsheet import read_rows


def df_to_Product(df, obj):
    """
    Converts the dataframe to a Product class
    :param:
        df (dataframe): Item from the Excel as a dataframe
        obj (Product): Object of the Product class

    """

    name = df["Nombre"].iloc[0]
    barcode = df["SKU"].iloc[0]
    price = df["Precio"].iloc[0]
    quantity = df["Cantidad"].iloc[0]
    category = df["Categoria"].iloc[0]

    product_obj = obj(name, barcode, price, quantity, category)

    return product_obj

def get_product(column, data):
    """
    Display the item to appear in the display at checking

    :param:
        column (str): String that shows the column of the file
        data (int): data of the product by SKU

    """
    df = read_rows(column, data)
    product_obj= df_to_Product(df, Product)
    return product_obj

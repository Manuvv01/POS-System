"""
Haandles conversion between DataFrame rows and Product objects
"""
import pandas
from ..models.product import Product

def df_to_Product(df,obj):
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


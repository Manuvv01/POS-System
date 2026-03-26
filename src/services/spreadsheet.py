"""
Handles operations on spreadsheets for the POS system.

This module provides functions to create, read, write, and update
product data in Excel or CSV format. It can be extended to support
additional spreadsheet operations as needed.
"""
import pandas as pd
import os
from crud import update

def get_path():
    # TODO: excl_file should be as input
    excl_file = "tortilleria.xlsx"
    file_path = "data/" + excl_file
    return file_path

def create_spreasdsheet():

    file_path = get_path()

    #dataframe creation
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns= ["Nombre","SKU", "Precio", "Cantidad", "Categoria"])
        df.to_excel(file_path, index= False)
        print("Archivo creado")
    else:
        print("El archivo ya existe")


def add_row(item):
    """"
        Adds a new item to the spreadsheet

    Args: item (Product): The item of a type class Product

    Returns:
        None

    """
    try:

        path = "data/tortilleria.xlsx" #Note: Make sure the path should be where it was excecuted
        df= pd.read_excel(path)

        new_product = {"Nombre": item.name,
                       "SKU": item.barcode,
                       "Precio": item.price,
                       "Cantidad":item.quantity,
                       "Categoria":item.category
        }

        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)

        df.to_excel(path, index=False)
        print("Excel updated successfully!")

    except FileNotFoundError:
        print("Error: File Not Found")

#TODO: Update spreadsheet
def update_spreadsheet():
    pass



#TODO: Delete spreadsheet




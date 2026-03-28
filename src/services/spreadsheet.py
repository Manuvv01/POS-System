"""
Handles operations on spreadsheets for the POS system.

This module provides functions to create, read, write, and update
product data in Excel or CSV format. It can be extended to support
additional spreadsheet operations as needed.
"""
from src.config import DATA_FILE
import pandas as pd
import os

def get_path():
    # TODO: excl_file should be as input
    excl_file = "tortilleria.xlsx"
    file_path = "data/" + excl_file
    return file_path

def create_spreasdsheet():
    """
    Checks if the spreadsheet, if not creates the file, if yes displays a message

    :return: None
    """

    file_path = get_path()

    #dataframe creation
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns= ["Nombre","SKU", "Precio", "Cantidad", "Categoria"])
        df.to_excel(file_path, index= False)
        print("Archivo creado")
    else:
        print("El archivo ya existe")


def read_rows(name):
    """"
        Adds a new item to the spreadsheet

    Args:
        name (str): The name of the product

    Returns:
        None

    """
    pass


def add_row(item):

    try:

        df= pd.read_excel(DATA_FILE)

        new_product = {"Nombre": item.name,
                       "SKU": item.barcode,
                       "Precio": item.price,
                       "Cantidad":item.quantity,
                       "Categoria":item.category
        }

        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)

        df.to_excel(DATA_FILE, index=False)
        print("Nueva Linea Agregada")

    except FileNotFoundError:
        print("Error: File Not Found")

#TODO: Update spreadsheet
def update_spreadsheet():
    """
    :param:
        None

    :return:
    """
    # Read the Excel and convert it to a Dataframe
    path = "data/tortilleria.xlsx"  # Note: Make sure the path should be where it was excecuted
    df = pd.read_excel(path)

    #get the old and new values.
    column = "Name"
    name = "Leche 1L"
    new = "Leche 500ml"

    # Update by name
    if column == 'Nombre':
        df.loc[df['Nombre'] == name, 'Nombre'] = new
    # Update by SKU
    elif column == 'SKU':
        df.loc[df['Nombre'] == name, 'SKU'] = new
    # Update by price
    elif column == 'Precio':
        df.loc[df['Nombre'] == name, 'Precio'] = new
    # Update by quantity
    elif column == 'Cantidad':
        df.loc[df['Nombre'] == name, 'Cantidad'] = new
    # Update by category
    elif column == 'Categoria':
        df.loc[df['Nombre'] == name, 'Categoria'] = new
    else:
        print("Columna no encontrada")

    #Save
    df.to_excel(path, index=False)

    print(f"{column} actualizado")

#TODO: Delete spreadsheet


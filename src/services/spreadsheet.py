"""
Handles operations on spreadsheets for the POS system.

This module provides functions to create, read, write, and update
product data in Excel or CSV format. It can be extended to support
additional spreadsheet operations as needed.
"""
from src.config import DATA_FILE
from src.utils.utilities import ensure_file_exists
import pandas as pd
import os

col = ["Nombre","SKU", "Precio", "Cantidad", "Categoria"]

#TODO: Delete this func and use ensure_file_exist in the other funcs
def get_path():

    excl_file = "tortilleria.xlsx"
    file_path = "data/" + excl_file
    return file_path


def create_spreasdsheet():
    """
    Gets the path where the file is going to be located. If the file doesn't exist in the path creates a Dataframe with
    their columns and saves it as an Excel, otherwise displays a message saying that the file exist.

    """

    file_path = get_path() # TODO: Debug

    #dataframe creation
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns= col) #Creates the columns
        df.to_excel(file_path, index= False)
        print("Archivo creado")
    else:
        print("El archivo ya existe")


def read_rows(column, data):
    """
    If the file exist reads it as a dataframe, if the column is not in the dataframe raises a value error, else locates
    the rows with the columns that contains the information, assign it in a variable and returns.

    :param:
        column (str): String that shows the column of the file
        data (int): data of the product by SKU

    """

    ensure_file_exists(DATA_FILE)
    df = pd.read_excel(DATA_FILE)

    #TODO: Make this a function in utils
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe.")

    search_row = df.loc[df[column] == data]

    return search_row



def add_row(item):
    """
    Reads the Excel file and converts it to a dataframe, creates a dictionary with the attributes of the Product class
    and assigns it in a variable then adds it to the dataframe and saves it in the Excel.

    :param:
        item: item of a Product class type

    """

    ensure_file_exists(DATA_FILE)

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


def update_spreadsheet():
    """
    Reads the file, takes the variable, updates the row depending on the column, saves and displays a message.

    """

    ensure_file_exists(DATA_FILE)
    df= pd.read_excel(DATA_FILE)

    #get the old and new values.
    column = "Name"
    name = "Leche 1L"
    new = "Leche 500ml"

    #TODO: Raise an exception if column is not in the dataframe

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
    df.to_excel(DATA_FILE, index=False)

    print(f"{column} actualizado")


def delete_row(column, name):
    """
    Deletes the index of the row in the dataframne by certain conditions.

    :param:
        column (str): A string that takes the name of the column
        info (str): Name of the data that needs to find

    """
    ensure_file_exists(DATA_FILE)
    df = pd.read_excel(DATA_FILE)

    #Deletes the index of the row that satisfy the condition

    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe.")
    else:
        df = df.drop(df[df[column] == name].index)
        df.to_excel(DATA_FILE, index=False)
        print("Linea borrada")

"""
Handles operations on spreadsheets for the POS system.

This module provides functions to create, read, write, and update
product data in Excel or CSV format. It can be extended to support
additional spreadsheet operations as needed.
"""
import pandas as pd
import os

def create_spreasdsheet():

    #TODO: excl_file should be as input
    excl_file = "tortilleria.xlsx"
    file_path = "../data/" + excl_file

    #dataframe creation
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns= ["Codigo de Barras", "Nombre","Precio", "Cantidad", "Categoria"])
        df.to_excel(file_path, index= False)
        print("Archivo creado")
    else:
        print("El archivo ya existe")

#TODO: Update spreadsheet

#TODO: Delete spreadsheet



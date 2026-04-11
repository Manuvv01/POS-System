"""
Contains file handlers for Tkinters
"""
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os

path = {"value": " "}

def save_file_dialog():
    """
    Opens a save file dialog and returns the selected file path.

    :return:  None
    """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if file_path:
        df = pd.DataFrame(columns=["Nombre", "SKU", "Precio", "Cantidad", "Categoria"])  # Creates the columns
        df.to_excel(file_path, index= False) #Creates the file
        path["value"] = file_path
        create_message= f"Archivo guardado en: {file_path}"
        messagebox.showinfo(title= "Archivo creado", message= create_message) #Prints message


def open_file_dialog(f_path):
    """
    Opens an Excel file from the specified file path.

    Args:
        f_path (str): Path to the Excel file.

    Returns:
        None
    """

    file_path = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if f_path:
        f_path["value"] = file_path
        os.startfile(file_path) #opens the file in the system

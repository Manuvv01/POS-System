"""
Contains file handlers for Tkinters
"""
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

path = {"value": " "}

def save_file_dialog():
    """
    Opens a save file dialog and returns the selected file path.

    :return: str | None
    """
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if file_path:
        df = pd.DataFrame(columns=["Nombre", "SKU", "Precio", "Cantidad", "Categoria"])  # Creates the columns
        df.to_excel(file_path, index= False) #Creates the file
        path["value"] = file_path
        print("Saved to:", file_path)
        create_message= f"Archivo guardado en: {file_path}"
        messagebox.showinfo(title= "Archivo creado", message= create_message) #Prints message


print(path)
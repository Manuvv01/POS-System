"""
UI Using TKINTER
"""
import tkinter as tk
from re import search

from src.services.outputs import display_scannedItem
from src.ui.handlers import add_to_textbox

def do_nothing():
    pass

def run_app():

    # Window creation
    root = tk.Tk()
    root.title("Punto de Venta")
    root.geometry("1200x650")

    #Textbox
    text_box = tk.Text(root, height= 17, width= 100, state= "disabled", font=("Arial", 20))
    text_box.grid(row= 0, column= 0, columnspan= 2, padx= 10, pady= 10, sticky= "w")

    #Barcode
    tk.Label(root, text= "SKU:", font=("Arial", 20)).grid(row= 1, column= 0, padx= 10, pady= 10, sticky= "w")
    barcode_entry = tk.Entry(root, width= 40, font=("Arial", 20))
    barcode_entry.grid(row=1, column=1, sticky="w")
    root.grid_columnconfigure(1, weight=1)
    barcode_entry.bind("<Return>",
                       func= lambda event: add_to_textbox(event, text_box, barcode_entry))

    # Buttons
    buttons_frame = tk.Frame(root)
    buttons_frame.grid(row=0, column=2, columnspan=3, sticky="nw", padx=10, pady=10)

    add_button = tk.Button(buttons_frame, text="Agregar", width=15, command=do_nothing)
    add_button.grid(row=0, column=0, padx=5)

    search_button = tk.Button(buttons_frame, text="Buscar", width=15, command=do_nothing)
    search_button.grid(row=0, column=1, padx=5)

    delete_button = tk.Button(buttons_frame, text="Borrar", width=15, command=do_nothing)
    delete_button.grid(row=0, column=2, padx=5)

    # Total Price section
    tk.Label(buttons_frame, text="Total", font=("Arial", 20)).grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0))
    total_price_box = tk.Text(buttons_frame, height=8, width=30, font=("Arial", 20))
    total_price_box.grid(row=2, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Change section
    tk.Label(buttons_frame, text="Change", font=("Arial", 20)).grid(row=3, column=0, columnspan=3, sticky="w")
    change_box = tk.Text(buttons_frame, height=5, width=30, font=("Arial", 20))
    change_box.grid(row=4, column=0, columnspan=3, sticky="w")

    root.mainloop()
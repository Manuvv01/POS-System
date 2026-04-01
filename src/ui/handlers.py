"""

This module contains event handler functions for the Tkinter UI.

Handlers are responsible for managing user interactions (such as key presses
or button clicks) and connecting those actions to the application’s business logic.
"""
import tkinter as tk
from src.services.outputs import display_scannedItem

def add_to_textbox(event, text_box, barcode_entry):
    column = "SKU"
    sku = int(barcode_entry.get().strip())  # Barcode from the entry
    item = display_scannedItem(column, data=sku)
    text_box.insert(tk.END, item + "\n")
    barcode_entry.delete(0, tk.END)  # clear input

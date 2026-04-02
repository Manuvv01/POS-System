"""

This module contains event handler functions for the Tkinter UI.

Handlers are responsible for managing user interactions (such as key presses
or button clicks) and connecting those actions to the application’s business logic.
"""
import tkinter as tk
from src.services.outputs import display_scannedItem
from src.utils.mappers import get_product


def add_to_textbox(event, text_box, barcode_entry):
    """
    Gets the barcode and displays the name and the price in the textbox

    :param
        text_box (tkinter): Textbox
        barcode_entry (tkinter): The entry for the barcode

    """
    NAME_WIDTH = 30
    PRICE_WIDTH = 8
    column = "SKU"
    sku = int(barcode_entry.get().strip())  #Barcode from the entry
    item = get_product(column, sku) #Product obj
    item_str = f"{item.name:<{NAME_WIDTH}} ${item.price:>{PRICE_WIDTH}.2f}"
    text_box.config(state="normal")  #Box typing is enable
    text_box.insert(tk.END, item_str + "\n")
    text_box.config(state="disabled")  #Box typing is disabled
    barcode_entry.delete(0, tk.END)  #Clear input

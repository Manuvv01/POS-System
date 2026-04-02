"""

This module contains event handler functions for the Tkinter UI.

Handlers are responsible for managing user interactions (such as key presses
or button clicks) and connecting those actions to the application’s business logic.
"""
import tkinter as tk
from src.utils.mappers import get_product
from src.services.cart_service import load_Cart



def scan_item(barcode_entry, cart):
    """
    Gets the item from the barcode and converts it as a Product saves it in the Cart class

    :param:
        barcode_entry (Tkinter): Input of the barcode
    :param:
        cart (Cart): Object of the Cart object
    :return:
        Item (Product): The item as a Product
    """

    column = "SKU"
    sku= int(barcode_entry.get().strip())  #Barcode from the entry
    item= get_product(column, sku) #Product obj
    load_Cart(item, cart)
    return item

def scanner_display(event, text_box, barcode_entry, cart, total, total_price_box):
    """
    Gets the barcode and displays the name and the price in the textbox

    :param
        text_box (tkinter): Textbox
        barcode_entry (tkinter): The entry for the barcode

    """

    ##ITEMS SCANNED SCREEN
    NAME_WIDTH= 30
    PRICE_WIDTH= 8
    item= scan_item(barcode_entry, cart) #Class Product
    item_str= f"{item.name:<{NAME_WIDTH}} ${item.price:>{PRICE_WIDTH}.2f}"
    text_box.config(state="normal")  #Box typing is enable
    text_box.insert(tk.END, item_str + "\n")
    text_box.config(state="disabled")  #Box typing is disabled
    barcode_entry.delete(0, tk.END)  #Clear input

    #TOTAL
    total["value"] += item.price

    total_price_box.config(state="normal")
    total_price_box.delete("1.0", tk.END)
    total_price_box.insert(tk.END, f"${total['value']:.2f}")
    total_price_box.config(state="disabled")

    barcode_entry.delete(0, tk.END)

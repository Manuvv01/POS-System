"""

This module contains event handler functions for the Tkinter UI.

Handlers are responsible for managing user interactions (such as key presses
or button clicks) and connecting those actions to the application’s business logic.
"""
import tkinter as tk
from tkinter import filedialog, Entry
from tkinter import messagebox
from src.utils.mappers import get_product
from src.services.cart_service import load_Cart
from src.utils.calculations import  calculate_total,calculate_change

label_font= ("Arial", 14)
button_font= ("Arial", 11)

def entries_actions(event, entry1, entry2, dic, key):
    """
    Assigns the value from an entry widget to a dictionary key
    and moves focus to the next entry field.

    Args:
        event: The Tkinter event that triggers the function.
        entry1: The current entry widget.
        entry2: The next entry widget to receive focus.
        dic (dict): Dictionary where the value will be stored.
        key (str): Key in the dictionary to assign the value to.

    Returns:
        None
    """
    dic[key] = entry1.get().strip()
    print(f"Saved {key}:", dic[key])

    entry2.focus()


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
    NAME_WIDTH= 43
    item= scan_item(barcode_entry, cart) #Class Product
    item_str= f"{item.name:<{NAME_WIDTH}} ${item.price:.2f}"
    text_box.config(state="normal")  #Box typing is enable
    text_box.insert(tk.END, item_str + "\n", "spaced")
    text_box.config(state="disabled")  #Box typing is disabled
    barcode_entry.delete(0, tk.END)  #Clear input

    #TOTAL
    calculate_total(total, item)

    total_price_box.config(state="normal")
    total_price_box.delete("1.0", tk.END)
    total_price_box.insert(tk.END, f"${total['value']:.2f}")
    total_price_box.tag_add("center", "1.0", "end") #Center on every insert
    total_price_box.config(state="disabled")

    barcode_entry.delete(0, tk.END)


def open_payment_window(root, total, change_box):
    """
    Opens a popup window that prompts the user to enter the amount of money
    provided for the transaction. Calculates the change based on the total
    and updates the change display in the main UI.

    :param: root (tk.Tk): The main application window used as the parent for the popup.
    :param: total (dict): A dictionary containing the current total price
    :param: change_box (tk.Text): The Text widget where the calculated change will be displayed.
    """
    #Change function
    cmd = lambda: process_payment(total = total, change_box= change_box, popup= popup,
                                               money_entry= money_entry)
    popup = tk.Toplevel(root)
    popup.title("Pago")
    popup.geometry("300x200")

    tk.Label(popup, text="Ingrese el dinero:", font= label_font).pack(pady=10)

    money_entry = tk.Entry(popup, font= label_font)
    money_entry.bind("<Return>", lambda event: cmd()) #Press Enter execute the function
    money_entry.pack(pady=10)

    tk.Button(popup, text="Confirmar", font= button_font, command= cmd).pack(pady=10)


def process_payment(total, change_box, popup, money_entry):
    """
    Processes the payment entered by the user in the popup window.
    Converts the input to a numeric value, calculates the change based
    on the current total, updates the change display in the main UI,
    and closes the popup window.

    If the input is invalid, an error message is displayed in the popup.

    :param: total (dict): A dictionary containing the current total price.
    :param: change_box (tk.Text): The Text widget where the calculated change will be displayed.
    :param: popup (tk.Toplevel): The popup window used for entering the payment.
    :param: money_entry (tk.Entry): The Entry widget where the user inputs the payment amount.
    """

    try:
        money = float(money_entry.get())
        change= calculate_change(money,total)

        # Update change box
        change_box.config(state="normal")
        change_box.delete("1.0", tk.END)
        change_box.insert(tk.END, f"${change:.2f}")
        change_box.tag_add("center", "1.0", "end")  # Center on every insert
        change_box.config(state="disabled")

        popup.destroy()     #Exit Popup

    except ValueError:
        tk.Label(popup, text="Entrada inválida", fg="red").pack()


def clear(entry):
    entry.delete(0, tk.END)

## ADD PRODUCT

def add_product(root):
    """
    Opens a Tkinter window that allows the user to input product details.

    Args:
        root: The parent Tkinter window.

    Returns:
        None
    """

    item ={'SKU': "",
           'Name': "",
           'Price': "",
           'Quantity': "",
           'Category':""}


    popup = tk.Toplevel(root, padx= 100, pady= 80)
    popup.title("Agregar Producto")
    popup.geometry("600x400")

    popup.transient(root)  # attach to main window
    popup.grab_set()    # modal behavior (locks focus)
    popup.focus_force() # bring to front

    #TODO: Input Validation
    #SKU
    tk.Label(popup, text="SKU:", font=label_font) \
    .grid(row= 0, column= 0)
    sku_entry = Entry(popup, font=label_font)
    sku_entry.grid(row= 0, column=  1, pady= 8)
    sku_entry.bind("<Return>", lambda event: entries_actions(event, entry1= sku_entry, entry2= name_entry,
                                                             dic= item, key='SKU'))
    #Nombre
    tk.Label(popup, text="Nombre:", font=label_font) \
    .grid(row= 1, column= 0)
    name_entry = Entry(popup, font=("Arial", 14))
    name_entry.grid(row= 1, column=  1, pady= 8)
    name_entry.bind("<Return>", lambda event: entries_actions(event, entry1= name_entry, entry2= price_entry,
                                                             dic= item, key='Name'))
    #Precio
    tk.Label(popup, text="Precio:", font=label_font) \
    .grid(row= 2, column= 0)
    price_entry = Entry(popup, font=label_font)
    price_entry.grid(row= 2, column=  1, pady= 8)
    price_entry.bind("<Return>", lambda event: entries_actions(event, entry1= price_entry, entry2= quantity_entry,
                                                             dic= item, key='Price'))
    #Cantidad
    tk.Label(popup, text="Cantidad:", font=label_font) \
    .grid(row= 3, column= 0)
    quantity_entry = Entry(popup, font=("Arial", 14))
    quantity_entry.grid(row= 3, column=  1, pady= 8)
    quantity_entry.bind("<Return>", lambda event: entries_actions(event, entry1= quantity_entry, entry2= cat_entry,
                                                             dic= item, key='Quantity'))
    #Categoria
    tk.Label(popup, text="Categoria:", font=label_font) \
    .grid(row= 4, column= 0)
    cat_entry = Entry(popup, font=("Arial", 14))
    cat_entry.grid(row= 4, column=  1, pady= 10)
    cat_entry.bind("<Return>", lambda event: confirmation_window(item,cat_entry, popup))

    # TODO: Create command for the button
    tk.Button(popup, text= "Confirmar", font= button_font, command= lambda : confirmation_window(item, cat_entry,
                                                                                                 popup)) \
    .grid(row= 5, column= 1)

def confirmation_window(dic, entry, popup):
    """
    Displays a confirmation window showing product information
    before adding it to the spreadsheet.

    Args:
        dic (dict): Dictionary containing the product data.
        entry: Tkinter entry widgets used for user input.
        popup: Tkinter window instance for the confirmation dialog.

    Returns:
        None
    """

    dic["Category"] = entry.get().strip()
    print(f"Saved Category:", dic["Category"])

    product_message= (f"SKU: {dic['SKU']}\n"
              f"Name: {dic['Name']}\n"
              f"Price: {dic['Price']}\n"
              f"Quantity: {dic['Quantity']}\n"
              f"Category: {dic['Category']}")

    result =messagebox.askyesno(
        "Confirmación",
        product_message,
        parent=popup
    )

    if result:
        print("Product confirmed ")
        # save to Excel or database here
    else:
        print("Go back")


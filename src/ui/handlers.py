"""

This module contains event handler functions for the Tkinter UI.

Handlers are responsible for managing user interactions (such as key presses
or button clicks) and connecting those actions to the application’s business logic.
"""
import tkinter as tk
from tkinter import Entry
from tkinter import messagebox
from src.utils.mappers import get_product
from src.services.cart_service import load_Cart
from src.utils.calculations import  calculate_total,calculate_change
from src.models.product import Product
from src.services.spreadsheet import add_row
from src.utils.utilities import center_window

labelentryfont= ("Arial", 14)
button_font= ("Arial", 11)
searchbox_font= ("Courier New", 14)
radiobutton_font= ("Arial", 16)



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

    tk.Label(popup, text="Ingrese el dinero:", font= labelentryfont).pack(pady=10)

    money_entry = tk.Entry(popup, font= labelentryfont)
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

## AGREGAR BUTTON COMMANDS

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

    center_window(parent= root, window= popup)

    #TODO: Input Validation
    #SKU
    tk.Label(popup, text="SKU:", font=labelentryfont).grid(row= 0, column= 0)
    sku_entry = Entry(popup, font=labelentryfont)
    sku_entry.grid(row= 0, column=  1, pady= 8)
    sku_entry.bind("<Return>", lambda event: entries_actions(event, entry1= sku_entry, entry2= name_entry,
                                                             dic= item, key='SKU'))
    #Nombre
    tk.Label(popup, text="Nombre:", font=labelentryfont).grid(row= 1, column= 0)
    name_entry = Entry(popup, font= labelentryfont)
    name_entry.grid(row= 1, column=  1, pady= 8)
    name_entry.bind("<Return>", lambda event: entries_actions(event, entry1= name_entry, entry2= price_entry,
                                                             dic= item, key='Name'))
    #Precio
    tk.Label(popup, text="Precio:", font=labelentryfont).grid(row= 2, column= 0)
    price_entry = Entry(popup, font=labelentryfont)
    price_entry.grid(row= 2, column=  1, pady= 8)
    price_entry.bind("<Return>", lambda event: entries_actions(event, entry1= price_entry, entry2= quantity_entry,
                                                             dic= item, key='Price'))
    #Cantidad
    tk.Label(popup, text="Cantidad:", font=labelentryfont).grid(row= 3, column= 0)
    quantity_entry = Entry(popup, font= labelentryfont)
    quantity_entry.grid(row= 3, column=  1, pady= 8)
    quantity_entry.bind("<Return>", lambda event: entries_actions(event, entry1= quantity_entry, entry2= cat_entry,
                                                             dic= item, key='Quantity'))
    #Categoria
    tk.Label(popup, text="Categoria:", font=labelentryfont).grid(row= 4, column= 0)
    cat_entry = Entry(popup, font=labelentryfont)
    cat_entry.grid(row= 4, column=  1, pady= 10)
    cat_entry.bind("<Return>", lambda event: confirmation_window(dic= item, sku_entry= sku_entry, name_entry= name_entry,
                                                    price_entry= price_entry, quantity_entry= quantity_entry,
                                                    cat_entry= cat_entry, popup= popup))

    # TODO: Create command for the button
    tk.Button(popup, text= "Confirmar", font= button_font,
              command= lambda : confirmation_window(dic= item, sku_entry= sku_entry, name_entry= name_entry,
                                                    price_entry= price_entry, quantity_entry= quantity_entry,
                                                    cat_entry= cat_entry, popup= popup)) \
    .grid(row= 5, column= 1)

def confirmation_window(dic, sku_entry, name_entry, price_entry, quantity_entry, cat_entry, popup):
    """
    Displays a confirmation dialog with product details before saving it to the spreadsheet.

    Args:
        dic (dict): Product data to be confirmed.
        sku_entry: Entry widget for the product SKU.
        name_entry: Entry widget for the product name.
        price_entry: Entry widget for the product price.
        quantity_entry: Entry widget for the product quantity.
        cat_entry: Entry widget for the product category.
        popup: Tkinter window instance for the dialog.

    Returns:
        None
    """

    # The user clicks confirm button it will create the dictionary
    if dic['SKU'] == "" and dic['Name'] == "" and dic['Price'] == "" and dic['Quantity'] == "":
        dic['SKU'] = sku_entry.get().strip()
        dic['Name'] = name_entry.get().strip()
        dic['Price'] = price_entry.get().strip()
        dic['Quantity'] = quantity_entry.get().strip()

    dic['Category'] = cat_entry.get().strip()

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
        #Creates the object
        product= Product(name= dic['Name'],
                         barcode= dic['SKU'],
                         price= dic['Price'],
                         quantity= dic['Quantity'],
                         category= dic['Category'])

        add_row(product) #Store it in the spreadsheet
        create_message= "El producto ha sido guardado"
        messagebox.showinfo(title="Producto Guardado", message=create_message)

    else:
        print("Go back")
        popup.focus_force() #Makes the entries window to not minimize


#BUSCAR BUTTON COMMANDS

def search_product(root):
    popup = tk.Toplevel(root, padx= 100, pady= 80)
    popup.title("Buscar Producto")
    width = 1600
    height = 800
    popup.geometry(f"{width}x{height}")

    popup.transient(root)  # attach to main window
    popup.grab_set()    # modal behavior (locks focus)
    popup.focus_force() # bring to front

    center_window(parent= root, window= popup)

    # ===== TOP FRAME (search controls) =====
    top_frame = tk.Frame(popup)
    top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    popup.grid_columnconfigure(0, weight=1)

    # Entry
    search_entry = tk.Entry(top_frame, font= labelentryfont, width=40)
    search_entry.grid(row=0, column=0, padx=5, sticky="w")
    search_entry.focus_set()

    # Search button
    search_button = tk.Button(top_frame, text="Buscar", font= button_font, width=15)
    search_button.grid(row=0, column=1, padx=5)

    # Radio buttons
    filter_options = tk.StringVar(value="todos")

    tk.Radiobutton(top_frame, text="Todos", variable=filter_options, value="todos", font= radiobutton_font,
                    command= lambda: choose(filter_options)) \
    .grid(row=0, column=2, padx=5)


    tk.Radiobutton(top_frame, text="SKU", variable=filter_options, value="sku", font= radiobutton_font,
                    command= lambda: choose(filter_options)) \
        .grid(row=0, column=3, padx=5)

    tk.Radiobutton(top_frame, text="Nombre", variable=filter_options, value="nombre", font= radiobutton_font,
                    command= lambda: choose(filter_options)) \
        .grid(row=0, column=4, padx=5)

    tk.Radiobutton(top_frame, text="Categoria", variable=filter_options, value="categoria", font= radiobutton_font,
                    command= lambda: choose(filter_options)) \
        .grid(row=0, column=5, padx=5)


    # ===== BOTTOM FRAME (results textbox) =====
    bottom_frame = tk.Frame(popup)
    bottom_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    popup.grid_rowconfigure(1, weight=1)  # makes textbox expand

    results_box = tk.Text(
        bottom_frame,
        font=searchbox_font,
        state="normal",
        padx= 10,
        pady= 10
    )
    results_box.pack(fill="both", expand=True)

def choose(filter_options):
    option = filter_options.get()
    if option == "todos":
        print("Is todos")
    elif option == "sku":
        print("Is sku")
    elif option == "nombre":
        print("Is nombre")
    elif option == "categoria":
        print("Is categoria")

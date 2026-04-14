"""
Inventory handlers module.

Contains event handler functions for managing product inventory,
including adding, updating, and deleting products through the UI.
"""
import tkinter as tk
from tkinter import Entry
from tkinter import messagebox
from src.models.product import Product
from src.services.product_storage import add_row
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


# =======AGREGAR BUTTON COMMANDS========

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
    width= 600
    height= 400
    popup.geometry(f"{width}x{height}")

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


#======BUSCAR BUTTON COMMANDS=========

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
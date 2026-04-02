"""
UI Using TKINTER
"""
import tkinter as tk
from src.ui.handlers import scanner_display
from src.models.cart import Cart

def do_nothing():
    pass

def run_app():

    cart = Cart() #Cart when scanning

    # Window creation
    root = tk.Tk()
    root.title("Punto de Venta")
    root.state("zoomed")

    #Textbox
    text_box = tk.Text(root, height= 17, width= 100, state= "disabled", font=("Courier New", 20))
    text_box.grid(row= 0, column= 0, columnspan= 2, padx= 10, pady= 10, sticky= "w")

    #Barcode
    tk.Label(root, text= "SKU:", font=("Arial", 20)).grid(row= 1, column= 0, padx= 10, pady= 10, sticky= "w")
    barcode_entry = tk.Entry(root, width= 40, font=("Arial", 20))
    barcode_entry.grid(row=1, column=1, sticky="w")
    root.grid_columnconfigure(1, weight=1)
    barcode_entry.bind("<Return>",
                       func= lambda event: scanner_display(event, text_box, barcode_entry, cart= cart))

    # Buttons
    buttons_frame = tk.Frame(root)
    buttons_frame.grid(row=0, column=2, columnspan=3, sticky="nw", padx=10, pady=10)

    add_button = tk.Button(buttons_frame,
                           text="Agregar",
                           width=15,
                           command=do_nothing)

    add_button.grid(row=0, column=0, padx=5)

    search_button = tk.Button(buttons_frame,
                              text="Buscar",
                              width=15,
                              command=do_nothing)

    search_button.grid(row=0, column=1, padx=5)

    delete_button = tk.Button(buttons_frame,
                              text="Borrar",
                              width=15,
                              command=do_nothing)

    delete_button.grid(row=0, column=2, padx=5)

    # Total Price section
    tk.Label(buttons_frame, text="Total", font=("Arial", 20)) \
        .grid(row=1, column=0, columnspan=3, sticky="w", pady=(10, 0))

    total_price_box = tk.Text(buttons_frame, height=4, width=30,
                              font=("Courier New", 20), state="disabled")
    total_price_box.grid(row=2, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Change section
    tk.Label(buttons_frame, text="Cambio", font=("Arial", 20)) \
        .grid(row=5, column=0, columnspan=3, sticky="w")

    change_box = tk.Text(buttons_frame, height=3, width=30,
                         font=("Courier New", 20), state="disabled")
    change_box.grid(row=6, column=0, columnspan=3, sticky="w")

    pay_button = tk.Button(
        buttons_frame,
        text= "Pagar",
        font= ("Arial", 16),
        width= 15,
        command= do_nothing
    )

    pay_button.grid(row=7, column=0, columnspan=3, pady=15)

    root.mainloop()
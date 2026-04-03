"""
UI Using TKINTER
"""
import tkinter as tk
import tkinter.messagebox
from src.ui.handlers import scanner_display, open_payment_window
from src.models.cart import Cart

def clear(entry):
    entry.delete(0, tk.END)


def do_nothing():
    pass


def run_app():

    cart = Cart()
    total = {"value": 0.0}

    # Window creation
    root = tk.Tk()
    root.title("Punto de Venta")
    root.state("zoomed")

    left_frame = tk.Frame(root)
    left_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

    # Textbox (items display)
    text_box = tk.Text(
        left_frame,
        height=30,
        width=85,
        state="disabled",
        font=("Courier New", 20)
    )
    text_box.grid(row=0, column=0, columnspan=3, pady=10, sticky="w")

    # Barcode row (grouped tightly)
    barcode_frame = tk.Frame(left_frame)
    barcode_frame.grid(row=1, column=0, sticky="w", pady=10)

    tk.Label(barcode_frame, text="SKU:", font=("Arial", 20)) \
        .pack(side="left", padx=(0, 5))

    barcode_entry = tk.Entry(barcode_frame, width=20, font=("Arial", 20))
    barcode_entry.pack(side="left", padx=(0, 5))

    tk.Button(barcode_frame, text="Clear", width=10, command=lambda: clear(barcode_entry)) \
        .pack(side="left")


    right_frame = tk.Frame(root)
    right_frame.grid(row=0, column=1, sticky="n", padx=10, pady=10)

    # Top buttons
    tk.Button(right_frame, text="Agregar", width=15, command=do_nothing)\
        .grid(row=0, column=0, padx=5)

    tk.Button(right_frame, text="Buscar", width=15, command=do_nothing)\
        .grid(row=0, column=1, padx=5)

    tk.Button(right_frame, text="Borrar", width=15, command=do_nothing)\
        .grid(row=0, column=2, padx=5)

    # Total
    tk.Label(right_frame, text="Total", font=("Arial", 20))\
        .grid(row=1, column=0, columnspan=3, sticky="w", pady=(15, 0))

    total_price_box = tk.Text(
        right_frame,
        height=4,
        width=30,
        font=("Courier New", 20),
        state="disabled"
    )
    total_price_box.grid(row=2, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Change
    tk.Label(right_frame, text="Cambio", font=("Arial", 20))\
        .grid(row=3, column=0, columnspan=3, sticky="w")

    change_box = tk.Text(
        right_frame,
        height=3,
        width=30,
        font=("Courier New", 20),
        state="disabled"
    )
    change_box.grid(row=4, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Pay button
    tk.Button(
        right_frame,
        text="Pagar",
        font=("Arial", 16),
        width=15,
        command=lambda: open_payment_window(root, total, change_box)
    ).grid(row=5, column=0, columnspan=3, pady=15)


    barcode_entry.bind(
        "<Return>",
        lambda event: scanner_display(
            event,
            text_box,
            barcode_entry,
            cart=cart,
            total=total,
            total_price_box=total_price_box
        )
    )

    root.mainloop()
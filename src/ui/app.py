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

    # ToolBar
    toolbar = tk.Frame(root, pady= 5, padx= 10 )
    toolbar.grid(row=0, column=0, columnspan=2, sticky="ew")

    tk.Button(toolbar, text="Crear", font=("Arial", 13)) \
        .grid(row=0, column=0, padx=5, pady=5)

    tk.Button(toolbar, text="Abrir", font=("Arial", 13)) \
        .grid(row=0, column=1, padx=5, pady=5)

    # Grid Column and Row
    root.grid_columnconfigure(0, weight=1)  # left expands
    root.grid_columnconfigure(1, weight=0)  # right stays fixed
    root.grid_rowconfigure(1, weight=1)


    # Left Frame
    left_frame = tk.Frame(root)
    left_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

    # Items display
    items_display = tk.Text(
        left_frame,
        height=21, #30
        width=57,#85
        state="disabled",
        font=("Courier New", 30) #20
    )
    items_display.grid(row=0, column=0, columnspan=3, sticky="w")
    items_display.tag_configure("spaced", spacing3=10)

    # Barcode row
    barcode_frame = tk.Frame(left_frame)
    barcode_frame.grid(row=1, column=0, sticky="w", pady=10)

    tk.Label(barcode_frame, text="SKU:", font=("Arial", 20)) \
        .pack(side="left", padx=(0, 5))

    barcode_entry = tk.Entry(barcode_frame, width=20, font=("Arial", 20))
    barcode_entry.pack(side="left", padx=(0, 5))

    tk.Button(barcode_frame, text="Clear", width=10, command=lambda: clear(barcode_entry)) \
        .pack(side="left")


    # Right Frame
    right_frame = tk.Frame(root)
    right_frame.grid(row=1, column=1, sticky="n", padx=10, pady=10)

    # Top buttons
    tk.Button(right_frame, text="Agregar", font=("Arial", 13), width=15, command=do_nothing)\
        .grid(row=0, column=0, padx=5)

    tk.Button(right_frame, text="Buscar",font=("Arial", 13), width=15, command=do_nothing)\
        .grid(row=0, column=1, padx=5)

    tk.Button(right_frame, text="Borrar", font=("Arial", 13),width=15, command=do_nothing)\
        .grid(row=0, column=2, padx=5)

    # Total Box
    tk.Label(right_frame, text="Total", font=("Arial", 20))\
        .grid(row=1, column=0, columnspan=3, sticky="w", pady=(15, 0))

    total_price_box = tk.Text(
        right_frame,
        height=1,
        width=11,
        font=("Courier New", 50, "bold"),
        state="disabled"
    )
    total_price_box.tag_configure("center", justify="center")  #Configures "center" to justify center
    total_price_box.grid(row=2, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Change Box
    tk.Label(right_frame, text="Cambio", font=("Arial", 20))\
        .grid(row=3, column=0, columnspan=3, sticky="w")

    change_box = tk.Text(
        right_frame,
        height=1,
        width=11,
        font=("Courier New", 50, "bold"),
        state="disabled"
    )

    change_box.tag_configure("center", justify="center") #Center the Text
    change_box.grid(row=4, column=0, columnspan=3, sticky="w", pady=(0, 10))

    # Pay button
    tk.Button(
        right_frame,
        text="Pagar",
        font=("Arial", 16),
        width=15,
        command=lambda: open_payment_window(root, total, change_box)
    ).grid(row=5, column=0, columnspan=3, pady=15)

    # When you press enter in barcode entry calls scanner_display
    barcode_entry.bind(
        "<Return>",
        lambda event: scanner_display(
            event,
            text_box= items_display,
            barcode_entry= barcode_entry,
            cart= cart,
            total= total,
            total_price_box= total_price_box
        )
    )

    root.mainloop()
"""
UI Using TKINTER
"""
import tkinter as tk
#from src.services.spreadsheet import

def run_app():

    def add_to_textbox(event):
        column= "SKU"
        sku = barcode_entry.get() #Barcode from the entry
        if sku.strip() != "":
            text_box.insert(tk.END, sku + "\n")
            barcode_entry.delete(0, tk.END)  # clear input


    # Window creation
    root = tk.Tk()
    root.title("POS System")
    root.geometry("1200x600")

    #Textbox
    text_box = tk.Text(root, height= 20, width= 60)
    #text_box.pack(side="left", anchor="n", padx= 10, pady= 10)
    text_box.grid(row= 0, column= 0, columnspan= 2, padx= 10, pady= 10, sticky= "w")

    #Barcode
    tk.Label(root, text= "Barcode:").grid(row= 1, column= 0, padx= 10, pady= 10, sticky= "w")
    barcode_entry = tk.Entry(root, width= 60)
    barcode_entry.grid(row=1, column=1,  pady=10, sticky="w")
    root.grid_columnconfigure(1, weight=1)

    barcode_entry.bind("<Return>", add_to_textbox)

    root.mainloop()


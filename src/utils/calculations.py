"""
Does the calculations of the project
"""
import tkinter as tk

def process_payment(total, change_box, popup, money_entry):
    """

    :param
        total:
         change_box:
         popup:
         money_entry:

    """

    try:
        money = float(money_entry.get())
        change = money - total["value"]

        # Update change box
        change_box.config(state="normal")
        change_box.delete("1.0", tk.END)
        change_box.insert(tk.END, f"${change:.2f}")
        change_box.config(state="disabled")

        popup.destroy()

    except ValueError:
        tk.Label(popup, text="Entrada inválida", fg="red").pack()
"""
Does the calculations of the project
"""
import tkinter as tk

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
        change = money - total["value"]

        # Update change box
        change_box.config(state="normal")
        change_box.delete("1.0", tk.END)
        change_box.insert(tk.END, f"${change:.2f}")
        change_box.tag_add("center", "1.0", "end")  # Center on every insert
        change_box.config(state="disabled")

        popup.destroy()     #Exit Popup

    except ValueError:
        tk.Label(popup, text="Entrada inválida", fg="red").pack()
import tkinter as tk

def do_nothing():
    pass

def run_app():
    # Window creation
    root = tk.Tk()
    root.title("POS System")
    root.geometry("400x300")

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Add Item", command= do_nothing)
    button.pack(pady=10)

    label = tk.Label(root, text="")
    label.pack(pady=10)

    root.mainloop()
"""
Functions that will help with development
"""
import os

def ensure_file_exists(path: str):
    """
    Ensures that a file exists at the given path.

    Args:
        path (str): The file path to check.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")


def center_window(parent, window):
    window.update_idletasks()

    width = window.winfo_width()
    height = window.winfo_height()

    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")
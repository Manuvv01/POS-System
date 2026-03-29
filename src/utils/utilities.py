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
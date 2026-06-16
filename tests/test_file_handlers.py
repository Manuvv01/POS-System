from unittest.mock import patch

from src.utils.file_handlers import save_file_dialog
from src.utils.file_handlers import path


@patch("src.utils.file_handlers.messagebox.showinfo")
@patch("pandas.DataFrame.to_excel")
@patch("src.utils.file_handlers.filedialog.asksaveasfilename")
def test_save_file_dialog_creates_file(mock_asksaveasfilename,mock_to_excel,mock_showinfo):
    """
    Tests that save_file_dialog() correctly creates an Excel file
    when the user selects a valid file path.

    This test verifies that:
        - The file dialog returns a valid path.
        - The Excel file creation method is called.
        - The global path variable is updated.
        - A success message is displayed to the user.

    Expected Result:
        - path["value"] contains the selected file path.
        - DataFrame.to_excel() is called once.
        - messagebox.showinfo() is called once.
    """
    # Arrange
    test_path = "inventory.xlsx"
    mock_asksaveasfilename.return_value = test_path

    # Act
    save_file_dialog()

    # Assert
    assert path["value"] == test_path

    mock_to_excel.assert_called_once_with(
        test_path,
        index=False
    )

    mock_showinfo.assert_called_once()


@patch("src.utils.file_handlers.messagebox.showinfo")
@patch("pandas.DataFrame.to_excel")
@patch("src.utils.file_handlers.filedialog.asksaveasfilename")
def test_save_file_dialog_cancelled(mock_asksaveasfilename,mock_to_excel,mock_showinfo):
    """
    Tests that save_file_dialog() performs no action when
    the user cancels the save dialog.

    This test verifies that:
        - No Excel file is created.
        - No success message is displayed.
        - The file creation method is never called.

    Expected Result:
        - DataFrame.to_excel() is not called.
        - messagebox.showinfo() is not called.
    """
    # Arrange
    mock_asksaveasfilename.return_value = ""

    # Act
    save_file_dialog()

    # Assert
    mock_to_excel.assert_not_called()
    mock_showinfo.assert_not_called()


from unittest.mock import patch

from src.utils.file_handlers import open_file_dialog


@patch("src.utils.file_handlers.os.startfile")
@patch("src.utils.file_handlers.filedialog.askopenfilename")
def test_open_file_dialog_opens_selected_file(
    mock_askopenfilename,
    mock_startfile
):
    """
    Tests that open_file_dialog() correctly updates the
    provided path dictionary and opens the selected file.

    This test verifies that:
        - A file path is returned by the file dialog.
        - The path dictionary is updated with the selected file path.
        - The operating system's file-opening function is called.

    Expected Result:
        - f_path["value"] contains the selected file path.
        - os.startfile() is called exactly once with the selected path.
    """

    # Arrange
    test_path = "inventory.xlsx"
    f_path = {"value": ""}

    mock_askopenfilename.return_value = test_path

    # Act
    open_file_dialog(f_path)

    # Assert
    assert f_path["value"] == test_path
    mock_startfile.assert_called_once_with(test_path)


@patch("src.utils.file_handlers.os.startfile")
@patch("src.utils.file_handlers.filedialog.askopenfilename")
def test_open_file_dialog_empty_dictionary(
    mock_askopenfilename,
    mock_startfile
):
    """
    Tests that open_file_dialog() performs no action when
    an empty dictionary is provided.

    This test verifies that:
        - The file dialog may return a file path.
        - The provided dictionary is not modified.
        - The file is not opened by the operating system.

    Expected Result:
        - os.startfile() is not called.
        - The dictionary remains empty.
    """

    # Arrange
    mock_askopenfilename.return_value = "inventory.xlsx"
    f_path = {}

    # Act
    open_file_dialog(f_path)

    # Assert
    mock_startfile.assert_not_called()
    assert f_path == {}
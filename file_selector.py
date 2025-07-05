# Selects a file using tkinter filedialog.
# Defaults to the current directory or passes in-path.

from tkinter import filedialog

def select_pdf_file(initialdir=None, parent=None):
    """
    Open a modal file-open dialog.
    • `parent` keeps the dialog on top of its caller.
    • `initialdir` lets the caller suggest a starting folder.
    """
    options = {
        "title": "Select a .txt file",           
        "filetypes": [("Text files", "*.txt")],  
    }
    if initialdir is not None:
        options["initialdir"] = initialdir
    if parent is not None:
        options["parent"] = parent

    return filedialog.askopenfilename(**options)

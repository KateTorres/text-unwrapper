# Selects a file using tkinter filedialog.
# Defaults to the current directory or passes in-path.

import os
import tkinter as tk
from tkinter import filedialog

def select_pdf_file(last_directory=os.getcwd()):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a .txt file",
        filetypes=[("Text Files", "*.txt")],
        initialdir=last_directory
    )
    return file_path
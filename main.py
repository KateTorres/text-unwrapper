# Orchestrates the workflow: file selection → text loading → unwrapping → saving.
# Notifies the user of start and completion.
# Delegates to modular utility functions.

import os
import sys
import tkinter as tk
from tkinter import messagebox
from file_selector import select_pdf_file

from utils.text_loader import load_text_file
from utils.text_unwrapper import unwrap_text
from utils.text_saver import save_text_file

def main():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Select File", "Please select a .txt file to unwrap.")
    file_path = select_pdf_file()
    if not file_path or not file_path.lower().endswith('.txt'):
        print("No .txt file selected. Exiting.")
        sys.exit(1)

    raw_text = load_text_file(file_path)
    unwrapped_text = unwrap_text(raw_text)
    save_text_file(unwrapped_text, file_path)
    messagebox.showinfo("Done", "Unwrapped text has been saved successfully.")

if __name__ == "__main__":
    main()

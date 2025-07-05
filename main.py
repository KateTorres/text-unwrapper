# Orchestrates the workflow: file selection → text loading → unwrapping → saving.
# Notifies the user of start and completion.
# Delegates to modular utility functions.
# Processing pass:
#    1. prompt for operation(s)
#    2. open a file-selection dialog (always on top)
#    3. load, process, save

import os
import tkinter as tk
from tkinter import messagebox

from file_selector import select_pdf_file            # existing selector
from utils.text_loader import load_text_file
from utils.text_unwrapper import unwrap_text
from utils.text_saver import save_text_file
from utils.file_handler import get_last_directory, save_last_directory
from utils.operation_menu import choose_operation    # new
from utils.bracket_number_remover import remove_bracket_numbers  # new


def main() -> None:
    root = tk.Tk()
    root.withdraw()          # keep the root window invisible
    root.update()            # finish Tk initialisation

    try:
        # 1. choose processing mode (console prompt)
        operation = choose_operation()

        # 2. pick the input file (dialog always on top)
        root.lift()
        root.attributes('-topmost', True)

        initial_dir = get_last_directory() or os.getcwd()
        file_path = select_pdf_file(initialdir=initial_dir, parent=root)
        root.attributes('-topmost', False)

        if not file_path:
            return
        save_last_directory(os.path.dirname(file_path))

        # 3. load, process, save
        text = load_text_file(file_path)

        if operation in ("remove_refs", "both"):
            text = remove_bracket_numbers(text)
        if operation in ("unwrap", "both"):
            text = unwrap_text(text)

        save_text_file(text, file_path)
        messagebox.showinfo("Done", "Processing complete.")
    finally:
        root.destroy()


if __name__ == "__main__":
    main()

# Text Unwrapper
This short python program unwraps line-wrapped `.txt` files by removing unnecessary line breaks. This can be useful for further processing, such as conversion of text into audio.
The program merges lines unless separated by an empty line (indicating a paragraph break). It uses a simple GUI prompt to select a `.txt` file and saves the result with a `_unwrapped.txt` suffix and provides user with an option to exclude bracketed numbers (for example: [123]).

## Features
- GUI-based file selection  
- Preserves paragraph break (user menu option)
- excludes bracketed numbers (user menu option)  
- Detects encoding with `chardet`
- Saves the unwrapped output to a new file  

## Usage
Run main.py (You can use .bat in Windows or .sh file in Linux)
    make sure to chmod +x run_unwrapper.sh
Use the file dialog to select the .txt file.
Find the unwrapped version saved in the same folder as the original file.

## Project Structure
```
text-unwrapper/
├── main.py
├── file_selector.py
├── run_unwrapper.bat
├── run_unwrapper.sh
├── requirements.txt
├── config.py
├── load_log.txt (auto-created)
├── utils/
│   ├── bracket_number_remover.py
│   ├── operations_menu.py
│   ├── file_handler.py
│   ├── text_loader.py
│   ├── text_unwrapper.py
│   ├── text_saver.py
│   └── logger.py
└── README.md
└── CHANGELOG.md
```

## Requirements
- Python 3.7+
- 'tkinter'
- 'chardet'

Install all dependencies with:
```bash
pip install -r requirements.txt
```
## License
MIT License

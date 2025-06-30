# Saves the new file with the consistent suffix.
# Uses default encoding from config.

import os
from config import DEFAULT_ENCODING, OUTPUT_SUFFIX

def save_text_file(text, original_path):
    base, _ = os.path.splitext(original_path)
    new_path = base + OUTPUT_SUFFIX
    with open(new_path, 'w', encoding=DEFAULT_ENCODING) as f:
        f.write(text)
    print(f"Unwrapped text saved to: {new_path}")

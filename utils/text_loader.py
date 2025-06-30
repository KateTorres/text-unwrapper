#handles file I/O:
### Detects encoding using chardet.
### Logs detected encoding.

import chardet
from utils.logger import log_encoding
from config import DEFAULT_ENCODING, DETECT_BYTES

def detect_encoding(file_path, num_bytes=DETECT_BYTES):
    with open(file_path, 'rb') as f:
        raw_data = f.read(num_bytes)
    result = chardet.detect(raw_data)
    return result['encoding'] or DEFAULT_ENCODING

def load_text_file(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding, errors='replace') as f:
        content = f.read()
    log_encoding(file_path, encoding)
    return content

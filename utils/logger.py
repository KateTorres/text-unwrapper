# Appends timestamped encoding info to load_log.txt.

import os
from datetime import datetime
from config import LOG_PATH

def log_encoding(file_path, encoding):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} | {os.path.basename(file_path)} | Encoding: {encoding}\n")

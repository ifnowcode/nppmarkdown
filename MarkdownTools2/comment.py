# apply_header_1.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_header(text, level):
    lines = text.splitlines()
    prefix = ">" * level + " "

    processed = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            processed.append(prefix + stripped)
        else:
            processed.append("")
    return "\r\n".join(processed)

# --- Execution for Notepad++ ---
text, start, end = get_selected_or_current_line()
result = process_header(text, 1)
editor.replaceSel(result)
# Ensure blank line after the inserted block
new_end = start + len(result)
ensure_blank_line_after(new_end)

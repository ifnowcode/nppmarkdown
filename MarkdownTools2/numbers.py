# apply_list.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_numbered_list(text):
    lines = text.splitlines()

    # remove empty lines
    non_empty = [line.strip() for line in lines if line.strip()]

    # prefix each line with incrementing numbers
    numbered = []
    n = 1
    for line in non_empty:
        numbered.append("  " + str(n) + ". " + line)
        n += 1

    return "\r\n\r\n".join(numbered)

# --- Execution for Notepad++ ---
text, start, end = get_selected_or_current_line()
result = process_numbered_list(text)

editor.replaceSel(result)

new_end = start + len(result)
ensure_blank_line_after(new_end)


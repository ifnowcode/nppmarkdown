# apply_list.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_list(text):
    """
    Convert selected text into a Markdown list.
    Rules:
      - Remove empty lines
      - Prefix each line with '  * '
      - Preserve original line order
    """
    lines = text.splitlines()

    # Remove empty lines
    non_empty = [line.strip() for line in lines if line.strip()]

    # Prefix each line
    listed = ["  * " + line for line in non_empty]

    return "\r\n\r\n".join(listed)

# --- Execution for Notepad++ ---
text, start, end = get_selected_or_current_line()
result = process_list(text)

editor.replaceSel(result)

# Ensure a blank line after the list
new_end = start + len(result)
ensure_blank_line_after(new_end)

# apply_codeblock.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_codeblock(text):
    """
    Wrap the selected text in triple backticks on their own lines.
    """
    return "```\r\n" + text.rstrip() + "\n```"

# --- Execution for Notepad++ ---
text, start, end = get_selected_or_current_line()
result = process_codeblock(text)

# Replace selection
editor.replaceSel(result)

# Ensure blank line after the inserted block
new_end = start + len(result)
ensure_blank_line_after(new_end)

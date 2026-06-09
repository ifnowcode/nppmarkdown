# apply_format_table.py
from Npp import editor
import re
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def normalize_row(line):
    stripped = line.strip()

    # Replace any run of 2+ spaces with a pipe
    parts = re.split(r'\s{2,}', stripped)

    # Join with pipes and wrap with leading/trailing pipe
    return "| " + " | ".join(parts) + " |"

def make_separator_from(row):
    sep = []
    for ch in row:
        if ch == "|":
            sep.append("|")
        else:
            sep.append("-")
    return "".join(sep)

def process_table(text):
    lines = [ln for ln in text.splitlines() if ln.strip()]

    if not lines:
        return ""

    formatted = [normalize_row(ln) for ln in lines]

    # Build separator line based on first formatted row
    separator = make_separator_from(formatted[0])

    return formatted[0] + "\r\n" + separator + "\r\n" + "\r\n".join(formatted[1:])

# --- Execution for Notepad++ ---
text, start, end = get_selected_or_current_line()
result = process_table(text)
editor.replaceSel(result)

new_end = start + len(result)
ensure_blank_line_after(new_end)

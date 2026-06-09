# apply_highlight.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_highlight(text):
    return "==" + text.strip() + "=="

text, start, end = get_selected_or_current_line()
result = process_highlight(text)

editor.replaceSel(result)

# apply_bold.py
from Npp import editor
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from common import *

def process_bold(text):
    return "**" + text.strip() + "**"

text, start, end = get_selected_or_current_line()
result = process_bold(text)

editor.replaceSel(result)

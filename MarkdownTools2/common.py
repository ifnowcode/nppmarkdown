# common.py
from Npp import editor

def get_selected_or_current_line():
    start = editor.getSelectionStart()
    end = editor.getSelectionEnd()

    if start != end:
        return editor.getSelText(), start, end

    # No selection - select the entire current line
    pos = editor.getCurrentPos()
    line_num = editor.lineFromPosition(pos)

    line_start = editor.positionFromLine(line_num)
    line_end = editor.getLineEndPosition(line_num)

    editor.setSelectionStart(line_start)
    editor.setSelectionEnd(line_end)

    text = editor.getSelText()
    return text, line_start, line_end

def ensure_blank_line_after(end_pos):
    """
    Ensures there is a blank line after the given position.
    """
    doc_length = editor.getTextLength()

    # If at end of document, append newline
    if end_pos >= doc_length:
        editor.insertText(end_pos, "\r\n")
        return

    # Determine next line
    next_line_num = editor.lineFromPosition(end_pos) + 1

    # If next line doesn't exist, append newline
    if next_line_num >= editor.getLineCount():
        editor.insertText(doc_length, "\r\n")
        return

    # Get next line text
    next_line_start = editor.positionFromLine(next_line_num)
    next_line_end = editor.getLineEndPosition(next_line_num)
    next_line_text = editor.getTextRange(next_line_start, next_line_end)

    # Insert blank line only if needed
    if next_line_text.strip() != "":
        editor.insertText(end_pos, "\r\n")
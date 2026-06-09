# Markdown Tools for Notepad++ — Installation & Setup Guide

These scripts add fast, deterministic Markdown editing tools to Notepad++ using the PythonScript plugin.

They support bold, italics, highlight, lists, numbered lists, code blocks, table formatting, and more.

Caveat: The table formatting isn't perfect but still helps.

These scripts were used to create this document in Notepad++.

---

## 1. Requirements

  * **Notepad++**

  * **PythonScript plugin (Python 2.7 edition)**

  Install via:
  **Plugins → Plugins Admin → PythonScript**

After installation, you will see:

Code
```
Plugins → PythonScript
```

You will need this to run these Python scripts.

---

## 2. Folder Structure

Place your scripts in the PythonScript `scripts` directory:

Commonly found at

Code
```
%AppData%\Notepad++\plugins\PythonScript\scripts\
```

>Important:  
>Scripts must be in the **top‑level `scripts/` folder** to appear in Shortcut Mapper.

## 3. Installing the Scripts

  1. Open the PythonScript scripts folder:

  Plugins → PythonScript → Scripts → Open Scripts Folder

  2. Copy all `.py` files (including `common.py`) into that folder.

  3. Restart Notepad++.

Your scripts now appear under:

Code
```
Plugins → PythonScript → Scripts
```

---

## 4. Registering Scripts as Menu Items

Notepad++ only exposes PythonScript scripts to Shortcut Mapper after they are registered.

To register:

  1. Go to Plugins → PythonScript → Configuration…

  2. Under Menu Items, click Add…

  3. Select a script (e.g., `bold.py`)

  4. Give it a readable name (e.g., “Markdown: Bold”)
  For me this just added the script path, I don't see a way to give it a readable name.

  5. Repeat for all scripts you want to bind

After registering, each script becomes a real menu command.

## 5. Assigning Keyboard Shortcuts

  1. Open Settings → Shortcut Mapper

  2. Go to the Plugin Commands tab

  3. Find your registered script (e.g., “Markdown: Bold”)

  4. Click Modify

  5. Assign a hotkey (e.g., `Ctrl+Alt+B`)

Your Markdown tools are now keyboard‑driven. 

Note: I found that the scripts must be in the top level scripts directory them to show up as menu items and in the shortcut mapper.

Here are my mappings:

  * bold.py       `Alt+S`

  * bullets.py    `Alt+B`

  * codeblock.py  `Alt+K`

  * comment.py    `Alt+Q`

  * header1.py    `Ctrl+Alt+Shift+1`

  * header2.py    `Ctrl+Alt+Shift+2`

  * header3.py    `Ctrl+Alt+Shift+3`

  * header4.py    `Ctrl+Alt+Shift+4`

  * header5.py    `Ctrl+Alt+Shift+5`

  * highlight.py  `Alt+L`

  * italics.py    `Alt+I`

  * numbers.py    `Alt+N`

  * table.py      `Alt+T`

---

## 6. Adding Scripts to the Right‑Click Context Menu

Note: I have not done this yet so these instructions are untested.

Edit (or create):

Code
```
%AppData%\Notepad++\contextMenu.xml
```

Add entries like:

xml
```
<Item PluginEntryName="PythonScript" PluginCommandItemName="Markdown: Bold" />
<Item PluginEntryName="PythonScript" PluginCommandItemName="Markdown: Italics" />
<Item PluginEntryName="PythonScript" PluginCommandItemName="Markdown: Code Block" />
```

Restart Notepad++ to apply changes.

---

## 7. Updating or Removing Scripts

To update a script:

  1. Replace the `.py` file in the `scripts/` folder

  2. Restart Notepad++ (or reload PythonScript)

To remove a script:

  1. Delete the `.py` file

  2. Remove its entry from PythonScript Configuration

  3. Remove any context‑menu entries

  4. Restart Notepad++
  
---

## 8. Troubleshooting

### Script not showing in Shortcut Mapper

  * It must be registered in PythonScript Configuration

  * It must be in the top‑level scripts/ folder

  * Restart Notepad++ after adding

### “ImportError: No module named common”

  * Ensure `common.py` is in the same folder as the scripts

  * Use:

  python
  ```
  from common import *
  ```

### Scripts not appearing in the PythonScript menu

  * Restart Notepad++

  * Ensure file extension is .py

  * Ensure PythonScript plugin is installed correctly

---

## Notes

I installed `MarkdownTools2` under scripts in it's own directory but then it didn't show up as menu items so I had to put them directly in the scripts folder. Last time I updated for some reason I had to update both directly under scripts and the `MarkdownTools2` folder. Modify the command (`.cmd`) scripts as needed to do this automatically for you. Currently they are for my local computer. Technically I think you only need them directly under the scripts folder but I did this backwards. Since this is working for me I don't feel like deleting and cleaning this out multiple times to test exactly how this works so you will have to figure this out. I'm giving this context in case it helps.

`install.cmd` will install a folder to scripts. E.g. `install MarkdownTools2`.
`copy2root.cmd` will install the target folder files to Notepad++ scripts root. E.g. `copy2root.cmd MarkdownTools2`'

These use the environment variable `_path_npp` to find the Notepad++ installation. Set this to the correct path in your environment or hard code in the script.

If you are not on Windows AI should be able to convert these scripts for you easily to bash etc.

You may have noticed this uses an older version of Python. I could not find or get a newer Python plugin for scripts. It's been a while so my memory isn't clear.
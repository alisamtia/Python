import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Muhammad Ali Samtia\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Muhammad Ali Samtia\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Remotesol_Pad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Remotesol Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons']}},
    version = "0.1",
    description = "This is A Professtional Text Editor You can also use it to Code Languages.",
    executables = executables
    )

import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Muhammad Ali Samtia\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Muhammad Ali Samtia\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Remotesol Image Resizer.py", base=base, icon="1.png")]


cx_Freeze.setup(
    name = "Remotesol Image Resizer",
    options = {"build_exe": {"packages":["tkinter","os","cv2","threading","customtkinter"], "include_files":["1.png",'tcl86t.dll','tk86t.dll']}},
    version = "1.00",
    description = "A Professtional Image Resizer",
    executables = executables
    )

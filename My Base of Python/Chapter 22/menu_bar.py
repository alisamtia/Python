import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title('Menu Bars')
def func():
    print('Hello')

# **************************************Simple Menu Bar******************************************************
# main_menu=tk.Menu(win)
# main_menu.add_command(label='File',command=func)
# main_menu.add_command(label='Save',command=func)
# main_menu.add_command(label='Save as',command=func)
# main_menu.add_command(label='Copy',command=func)
# main_menu.add_command(label='Paste',command=func)
# win.config(menu=main_menu)

main_menu=tk.Menu(win)
# tearoff to remove border
file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save',command=func)
file_menu.add_command(label='Save as',command=func)
main_menu.add_cascade(label='File',menu=file_menu)
win.config(menu=main_menu)

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Copy',command=func)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)
edit_menu.add_command(label='Bold',command=func)
main_menu.add_cascade(label='Edit',menu=edit_menu)

win.mainloop()
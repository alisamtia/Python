from tkinter import ttk
from tkinter import messagebox,colorchooser,filedialog,font
import tkinter as tk
import os

main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title('Remotesol Text Editor')
main_application.wm_iconbitmap('icon.ico')

# ########################################## Main Menu ####################################################
main_menu=tk.Menu()

########File
file=tk.Menu(main_menu,tearoff=False)
#icons
new_icon=tk.PhotoImage(file=r'icons\new.png')
open_icon=tk.PhotoImage(file='icons\open.png')
save_icon=tk.PhotoImage(file='icons\save.png')
save_as_icon=tk.PhotoImage(file='icons\save_as.png')
exit_icon=tk.PhotoImage(file='icons\exit.png')







#######Edit
edit=tk.Menu(main_menu,tearoff=False)
# Icons
copy_icon=tk.PhotoImage(file=r'icons\copy.png')
paste_icon=tk.PhotoImage(file=r'icons\paste.png')
cut_icon=tk.PhotoImage(file=r'icons\cut.png')
clear_all_icon=tk.PhotoImage(file=r'icons\clear_all.png')
find_icon=tk.PhotoImage(file=r'icons\find.png')


########View
view=tk.Menu(main_menu,tearoff=False)
#icons
tool_bar_icon=tk.PhotoImage(file=r'icons\tool_bar.png')
status_bar_icon=tk.PhotoImage(file=r'icons\status_bar.png')


####Color Theme
color_theme=tk.Menu(main_menu,tearoff=False)
#icons
light_default_icon=tk.PhotoImage(file=r'icons\light_default.png')
light_plus_icon=tk.PhotoImage(file=r'icons\light_plus.png')
dark_icon=tk.PhotoImage(file=r'icons\dark.png')
red_icon=tk.PhotoImage(file=r'icons\red.png')
monokai_icon=tk.PhotoImage(file=r'icons\monokai.png')
night_blue_icon=tk.PhotoImage(file=r'icons\night_blue.png')

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#FFFFFF'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#FFFFFF','#000000'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2'),
}


####cascade:
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
# ..............................&&&&&&&&&&&& END Main Menu &&&&&&&&&&&&&&&.................................
# ########################################## Toolbar ####################################################
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(column=0,row=0,padx=5)

# size box
size_var=tk.IntVar()
va=tuple(range(8,80,2))
font_size=ttk.Combobox(tool_bar,width=14,state='readonly',textvariable=size_var,value=va)
font_size.grid(column=1,row=0)
font_size.current(4)



#####bold button
bold_icon=tk.PhotoImage(file=r'icons\bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

#####Italic Button
italic_icon=tk.PhotoImage(file=r'icons\italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

#####underline button
underline_icon=tk.PhotoImage(file=r'icons\underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)


#### Font Color Button
font_color_icon=tk.PhotoImage(file=r'icons\font_color.png')
font_color=ttk.Button(tool_bar,image=font_color_icon)
font_color.grid(column=6,row=0)

# align left
align_left_icon=tk.PhotoImage(file=r'icons\align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(column=7,row=0,padx=5)

# align Center
align_center_icon=tk.PhotoImage(file=r'icons\align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(column=8,row=0,padx=5)

# align right
align_right_icon=tk.PhotoImage(file=r'icons\align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(column=9,row=0,padx=5)

asaw=ttk.Label(tool_bar,text='')
asaw.grid(column=10,row=0,padx=300)

#small
small_icon=tk.PhotoImage(file=r'icons\small.png')
small_btn=ttk.Button(tool_bar,image=small_icon)
small_btn.grid(column=11,row=0,padx=5)

# capital
capital_icon=tk.PhotoImage(file=r'icons\capital.png')
capital_btn=ttk.Button(tool_bar,image=capital_icon)
capital_btn.grid(column=12,row=0,padx=5)

#capitalize
capitaliz_icon=tk.PhotoImage(file=r'icons\capitaliz.png')
capitaliz_btn=ttk.Button(tool_bar,image=capitaliz_icon)
capitaliz_btn.grid(column=13,row=0,padx=5)

# ..............................&&&&&&&&&&&& END Toolbar &&&&&&&&&&&&&&&.................................
# ########################################## Text Editor ####################################################

text_editor=tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)



scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family='Arial'
current_font_size=12

def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fsize(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))



font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fsize)

text_editor.config(font=('Arial',12))

def make_bold():
    property=tk.font.Font(font=text_editor['font']).actual()
    if property['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if property['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=make_bold)

def make_italic():
    property=tk.font.Font(font=text_editor['font']).actual()
    if property['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if property['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))

italic_btn.configure(command=make_italic)

# Underline Functionality
def make_underline():
    property=tk.font.Font(font=text_editor['font']).actual()
    if property['underline']==False:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if property['underline']==True:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=make_underline)

def font_color_change():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color.configure(command=font_color_change)

def btn_align_left():
    content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,content,'left')

align_left_btn.configure(command=btn_align_left)


def btn_align_center():
    content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,content,'center')

align_center_btn.configure(command=btn_align_center)




def btn_align_right():
    content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,content,'right')

align_right_btn.configure(command=btn_align_right)



def btn_small():
    content=text_editor.get(1.0,'end')
    text_editor.delete(1.0,tk.END)
    content=content.lower()
    text_editor.insert(tk.INSERT,content)

small_btn.configure(command=btn_small)

def btn_capital():
    content=text_editor.get(1.0,'end')
    text_editor.delete(1.0,tk.END)
    content=content.upper()
    text_editor.insert(tk.INSERT,content)

capital_btn.configure(command=btn_capital)


def btn_capitaliz():
    content=text_editor.get(1.0,'end')
    text_editor.delete(1.0,tk.END)
    content=content.title()
    text_editor.insert(tk.INSERT,content)

capitaliz_btn.configure(command=btn_capitaliz)


# ..............................&&&&&&&&&&&& END Text Editor &&&&&&&&&&&&&&&................................
# ########################################## Status Bar ####################################################

status_bar=ttk.Label(main_application)
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        chars=len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f"Characters: {chars}   Words:{words}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>",changed)

# ..............................&&&&&&&&&&&& END Status Bar &&&&&&&&&&&&&&&.................................
# ########################################## Main Menu functionality ####################################################

# New file
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
    main_application.title('Remotesol Text Editor')


#File Commands
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

# Open file

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Please Select a File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    url
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        messagebox.showerror('From Remotesol Pad','File Not Found')
    else:
        main_application.title(os.path.basename(url))


file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

def save(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            os.chdir(url)
            print(os.getcwd())
            url.write(content2)
            url.close()
    except:
        return



file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save)

def save_as(event=None):
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
        os.chdir(url)
        print(os.getcwd())
    except:
        return 


file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the File?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)
#Edit Commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))

# find

def find_fu(event=None):
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find/Replace')
    find_dialogue.resizable(0,0)

    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matche=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matche+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    

    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    # frames
    find_frame=tk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_replace_label=ttk.Label(find_frame,text='Replace : ')

    # entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    # button
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)

    # Label and frame grid and button grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_button.grid(row=2,column=0,padx=4,pady=4)
    replace_button.grid(row=2,column=1,padx=4,pady=4)

    find_dialogue.mainloop()

edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_fu)
#view Commands
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_statusbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else :
        text_editor.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        tool_bar.pack(side=tk.TOP)
        show_toolbar=True
        


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack_forget()
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
# Color Theme Commands
def change_theme():
    choosen_theme=theme_choice.get()
    color_tuple=color_dict.get(choosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

main_application.config(menu=main_menu)
# ..............................&&&&&&&&&&&& END Main Menu functionality &&&&&&&&&&&&&&&.................................

#Bind ShortCut Keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit_func)

def wal(event=None):
    text_editor.delete(1.0,tk.END)

# Edit
main_application.bind("<Control-Alt-c>",wal)
main_application.bind("<Control-f>",find_fu)

main_application.mainloop()
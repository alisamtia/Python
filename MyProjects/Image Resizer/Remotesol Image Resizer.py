from tkinter.filedialog import askdirectory
import tkinter as tk
from tkinter import ttk,messagebox
import os
import cv2
import threading
from customtkinter import *
radio_group,path,out_path,progress_bar,width,height="","","","","",""

class ProgressBar(tk.Frame):
    def __init__(self, master, total=100, width=300, height=20, bg='white', fillcolor='green'):
        super().__init__(master)
        self.master = master
        self.total = total
        self.width = width
        self.height = height
        self.bg = bg
        self.fillcolor = fillcolor
        self.progress = 0
        self.create_widgets()
        
    def create_widgets(self):
        # Create the progress bar canvas
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg, highlightthickness=0)
        self.canvas.pack()
        # Draw the progress bar background
        self.bg_rect = self.canvas.create_rectangle(0, 0, self.width, self.height, fill=self.bg)
        # Draw the progress bar fill
        self.fill_rect = self.canvas.create_rectangle(0, 0, 0, self.height, fill=self.fillcolor)
        
    def update(self, value):
        # Update the progress bar with the new value
        self.progress = value
        fill_width = int((self.progress / self.total) * self.width)
        self.canvas.coords(self.fill_rect, 0, 0, fill_width, self.height)
        
    def zero(self, value):
        # Update the progress bar with the new value
        self.progress = 0
        fill_width = int((self.progress / self.total) * self.width)
        self.canvas.coords(self.fill_rect, 0, 0, 0, 0)

def reuseali():
    global radio_group,path,out_path,progress_bar,width,height


    path=""
    out_path=""

    def open_file(event=None):
        global path
        path = askdirectory(title='Select Folder') # shows dialog box and return the path

    def output_path(event=None):
        global out_path
        out_path = askdirectory(title='Select Folder') # shows dialog box and return the path

    # pip install customtkinter
    wn=CTk()
    wn.title("Modren GUI")
    set_appearance_mode("dark") #Dark, system, Light
    set_default_color_theme("green") #blue,green,dark-blue

    frame=CTkFrame(wn)
    frame.pack(padx=60,pady=20,expand=1,fill=BOTH)

    label=CTkLabel(frame,text="Image Resizer",font=("Arial",25,"bold"))
    label.pack(padx=10,pady=12)

    raw_height=StringVar()
    raw_width=StringVar()

    l1=CTkLabel(frame,text="Width: ",text_color="white")
    l1.pack(padx=0,pady=0)
    widthLabel=CTkEntry(frame,placeholder_text="Width",textvariable=raw_width)
    widthLabel.pack(padx=10,pady=12)

    l2=CTkLabel(frame,text="Height: ",text_color="white")
    l2.pack(padx=0,pady=0)
    heightLabel=CTkEntry(frame,placeholder_text="Height",placeholder_text_color="red",textvariable=raw_height)
    heightLabel.pack(padx=10,pady=12)

    choosefile=CTkButton(frame,text="Choose File",command=open_file)
    choosefile.pack(padx=10,pady=12)

    outputfolder=CTkButton(frame,text="Output Path",command=output_path)
    outputfolder.pack(padx=10,pady=12)



    radio_group = IntVar()

    # create radio buttons
    radio_button_1 = CTkRadioButton(frame, text="PNG", variable=radio_group, value=1)
    radio_button_2 = CTkRadioButton(frame, text="JPG", variable=radio_group, value=2)

    # pack radio buttons into root window
    radio_button_1.pack()
    radio_button_2.pack()



    def resize_images():
        
        comp=CTkLabel(frame,text="Completed Percentage",font=("Arial",25,"bold"))
        comp.pack()
        
        format="png"
        global radio_group
        global path, width, height, out_path
        width = int(raw_width.get())
        height = int(raw_height.get())

        # try:
        all_images = os.listdir(path)
        for i in range(len(all_images)):
            img = cv2.imread(f"{path}\\{all_images[i]}")
            img = cv2.resize(img, (width, height))

            if radio_group.get()==1:
                format="png"
            if radio_group.get()==2:
                format="jpg"
                
            cv2.imwrite(f'{out_path}\\{i}.{format}', img)
            

            comp.configure(text=f'{int((i/len(all_images))*100)}% Completed')
            
            progress_bar.update(i)
            progress_bar.update_idletasks()
            
            if len(all_images)==i+1:
                wn.after(10, wn.destroy)
                
                

    def submita():
        global progress_bar
        all_images=os.listdir(path)
        progress_bar = ProgressBar(frame, total=len(all_images), width=300, height=20, bg='white', fillcolor='#2FA572')
        progress_bar.pack(pady=10)
        
        t = threading.Thread(target=resize_images)
        t.start()
                
        
        
        

    submit=CTkButton(frame,text="Submit",command=submita)
    submit.pack(padx=10,pady=12)

    wn.geometry("400x550+90+90")
    wn.mainloop()

reuseali()

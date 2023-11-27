# pip install textblob
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from textblob import TextBlob


class spell:
    def __init__(self,window):
        self.text=ScrolledText(window)
        self.text.bind("<KeyRelease>",self.check)
        self.text.pack()
        self.fullstop=0

    def check(self,event):
        # print("Key is Pressed.")
        content=self.text.get("1.0",END)
        full_stop_count=content.count(".")

        if self.fullstop!=full_stop_count:
            self.fullstop=full_stop_count
            for word in content.split("."):
                self.text.delete("1.0",END)
                correct_spell=TextBlob(content)
                self.text.insert("1.0",correct_spell.correct())
                print(word)

root=Tk()
root.title("Real Time Spelling Checker and Corrector")
gui=spell(root)
root.geometry("400x500+120+120")
root.mainloop()
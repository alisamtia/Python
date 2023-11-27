# pip install pyttsx3
# pip install pypdf2
import pyttsx3
import PyPDF2

speaker=pyttsx3.init()

book=open("a.pdf","rb")
reader=PyPDF2.PdfFileReader(book)
no_of_page=reader.numPages
# print(no_of_page)

# text="Hello My name is Muhammad Ali."
for i in range(4,no_of_page):
    page=reader.getPage(i)
    text=page.extractText()
    speed=speaker.getProperty('rate')
    speaker.setProperty('rate',180)
    speaker.say(text)
speaker.runAndWait()
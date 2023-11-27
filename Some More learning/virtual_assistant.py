# pip install pyttsx3
# $ pip install speechrecognition==3.8.1
# pip install pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audiovoice):
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<11:
        return "Good Morning"
    if hour>=11 and hour<15:
        return "Good After Noon"
    if hour>=15 and hour<24:
        return "Good Evening"

def takevoicecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("Compiling Your Voice...Please Wait.....")
            text=r.recognize_google(audio,language='en-in')
            print(text)
        except:
            speak("Unable to Recognize your voice")
            takevoicecommand()
        return text
    


# speak("Hello, My name is ALi")

try:
    gre=greet()
    speak(f"I am your Personal Assistant. \nMy name is Jaclyn. \nPlease Enter your Name:")
    name=takevoicecommand()
    speak(f"{gre} {name}")
except:
    speak("I can't Under Stand Please Speak Again")

if __name__=='__main__':
    while True:
        work=takevoicecommand().lower()
        if 'how are you' in work:
            speak("I am Fine.")
            speak("How are You sir.")
        
        elif 'fine' in work:
            speak("It is Good to Know that You are Fine.")
        elif 'not fine' in work:
            speak("OH, No Its so Sad to Know that you are Not Fine.") 

        elif "who is our god" in work:
            speak("There is No God but One Allah.")
        
        elif "total number of islamic books" in work:
            speak("There are 4 Islamic Books in Islam")

        elif "name of all islamic book" in work:
            speak("Turat\nInjil\nZaboor\nQuran-e-Majid")
        
        elif "what is ramzan" in work:
            speak("Ramzan is the best Month of Year.")

        elif "open notepad" in work:
            speak("Opening Notepad")
            path=r"C:\Windows\System32\notepad.exe"
            os.startfile(path)
        
        elif "close notepad" in work:
            speak("Closing Notepad")
            os.system("TASKKILL /F /IM notepad.exe")


        elif "open my website" in work:
            speak("Opening Chrome")
            # url="catvidshd.com"
            # path="C:/Program Files/Google/Chrome/Application/chrome.exe"
            webbrowser.open('http://https://catvidshd.com/', new=2)
        
        elif "close chrome" in work:
            speak("Closing Chrome")
            path=r"TASKKILL /F /IM chrome.exe"

        elif 'goodbye' in work:
            speak(f"Bye {name}.. Have a Good {gre}, See You Again.")
            exit()
        
        else:
            speak("I can't Under Stand Please Speak Again")


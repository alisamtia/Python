# pip install SpeechRecognition
# pip install pyAudio
import speech_recognition as sr

voice=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    audio=voice.listen(source)
    try:
        text=voice.recognize_google(audio)
        print(f"Your Said: {text}")
    except:
        print("Your voice is not CLear")

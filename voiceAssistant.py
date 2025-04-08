import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
import os
from tkinter import *
import wikipedia
import tkinter.messagebox
import time
import speech_recognition as ar

while True:
    r = sr.Recognizer();
    with sr.Microphone as source:
        print("speak somthing....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if(text == "stop"):
                break
            else:
                window.Tk()
                window.geometry("700x600")
                
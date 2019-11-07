# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import ttk, Text
import speech_recognition as sr
import time
from src.main_control.main_execute_controller import execute

#Speech to text
rec = sr.Recognizer()
mic = sr.Microphone()


def parse():
    text=""
    with mic as source:
        #voice.configure(text="Hmm...", image=blue)
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)
    try:
        #voice.configure(text="Hmm...", image=blue)
        text = rec.recognize_google(audio, language="vi-VN")
    except sr.UnknownValueError or sr.RequestError:
        #voice.configure(text="Voice", image=red)
        return (False ,"Không nhận dạng được!")
    if text=="":
        #voice.configure(text="Voice", image=red)
        return (False ,"Không nhận dạng được!")
    #voice.configure(text="Voice", image=red)
    return (True, text)
#

ass = tk.Tk() 
ass.title("000 Assistance")
#ass.geometry("300x300")
ass.resizable(False, False)
ass.configure(background="black")


##Functions
def ask():
    voice.configure(text="Voice", image=red)
    voice.config(relief="sunken")
    text.configure(state="disabled")
    said.grid_remove()
    hi = parse()
    print(hi)
    if hi[0]:
        said.configure(text="Bạn vừa nói: "+ hi[1])
    else:
        said.configure(text="Xin lỗi, "+hi[1])
    said.grid(column=0, row=1, pady=20, columnspan=5)
    text.configure(state="active")


def noVoice():
    voice.configure(state="disabled")
    said.grid_remove()
    entry.grid(column=0, row=1)
    action.grid(column=1, row=1)


def typeText():
    entry.grid_remove()
    action.grid_remove()
    voice.configure(state="active")
    if value.get():
        print(execute(str(value.get())))
        said.configure(text="Bạn vừa nhập: "+value.get())
        said.grid(column=0, row=1, pady=20, columnspan=5)

##Attributes
#icon
green = tk.PhotoImage(file= r"./../icon/green.png")
red = tk.PhotoImage(file = r"./../icon/red.png")
blue = tk.PhotoImage(file = r"./../icon/blue.png")
#Green Button
text = tk.Button(ass, text="Text", image=green, compound="center", foreground="white", command=noVoice)
text.grid(column=0, row=0, padx=5)
#Red Button 
voice = tk.Button(ass, text="Voice", image=red, compound="center", foreground="white", command=ask)        
voice.grid(column=1, row=0, padx=5)
#TypeText
value = tk.StringVar()
entry = tk.Entry(ass, textvariable=value, width=10)
action = tk.Button(ass, text="OK", command=typeText)
#Result
said = tk.Label(wraplength=200)
ass.mainloop()

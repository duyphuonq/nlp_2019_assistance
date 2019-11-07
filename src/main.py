import tkinter as tk
from tkinter import ttk, Text
import speech_recognition as sr
import time
import text2speech
#Speech to text
rec = sr.Recognizer()
mic = sr.Microphone()
#

ass = tk.Tk() 
ass.title("000 Assistance")
#ass.geometry("300x300")
ass.resizable(False, False)
ass.configure(background="black")
cnt = 0
##Functions
def ask():
    global cnt
    txt = ""
    voice.configure(text="Hmm...", image=blue)
    voice.config(relief="sunken")
    text.configure(state="disabled")
    said.grid_remove()
    cnt += 1
    said.configure(text="Ấn nút màu xanh để ghi âm")
    said.grid(column=0, row=1, pady=20, columnspan=5)
    if cnt == 2:
        with mic as source:
            rec.adjust_for_ambient_noise(mic)
            audio = rec.listen(mic)
        try:
            txt = rec.recognize_google(audio, language="vi-VN")
        except sr.UnknownValueError or sr.RequestError:
            txt = "Không nhận dạng được!"
        said.configure(text=txt)
        voice.configure(text="Voice", image=red)
        said.grid(column=0, row=1, pady=20, columnspan=5)
        text2speech.speak(txt)
        text.configure(state="active")
        cnt = 0

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
        said.configure(text="Bạn vừa nhập: "+value.get())
        said.grid(column=0, row=1, pady=20, columnspan=5)

##Attributes
#icon
green = tk.PhotoImage(file= r"icon/green.png")
red = tk.PhotoImage(file = r"icon/red.png")
blue = tk.PhotoImage(file = r"icon/blue.png")
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

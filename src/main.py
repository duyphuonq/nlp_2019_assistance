# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import time
from src.main.main_execute_controller import execute
import text2speech
import os
import threading

#------------------------------------------------------------------------------#

#Speech to text
rec = sr.Recognizer()
mic = sr.Microphone()
#------------------------------------------------------------------------------#
#UI
ass = tk.Tk() 
ass.title("001 Assistance")
#ass.geometry("300x300")
ass.resizable(False, False)
ass.configure(background="black")
cnt = 0
#------------------------------------------------------------------------------#
##Functions
def ask():      #Call when click Blue button 
    global cnt
    txt =""
    cnt += 1
    voice.configure(text="Hmm...", image=blue)      #Change texture 
    voice.config(relief="sunken")       #Don't bother
    text.configure(state="disabled")    #Disable Green Button
    said.grid_remove()      #Disable text you just said
    said.configure(text="Ấn nút màu xanh để ghi âm")    #Enable Blue Button
    said.grid(column=0, row=1, pady=20, columnspan=5)
    if cnt == 2:
        os.system("mpg321 sounds/record-begin.mp3")
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
        text.configure(state="active")
        cnt = 0
    if len(txt) > 0:
        os.system("mpg321 sounds/record-end.mp3")
        tell = execute(txt)
        t1 = threading.Thread(target=cowsay, args=(tell,))
        t2 = threading.Thread(target=text2speech.speak, args=(tell,))
        t2.start()
        t1.start()
        t1.join()
        t2.join()


def noVoice():
    voice.configure(state="disabled")
    said.grid_remove()
    entry.grid(column=0, row=1)
    action.grid(column=1, row=1)


def cowsay(tell):
    os.system("xcowsay {}".format(tell))

def typeText():
    entry.grid_remove()
    action.grid_remove()
    voice.configure(state="active")
    if value.get():
        tell = execute(str(value.get()))
        t1 = threading.Thread(target=cowsay, args=(tell,))
        t2 = threading.Thread(target=text2speech.speak, args=(tell,))
        t2.start()
        t1.start()
        t1.join()
        t2.join()
        said.configure(text="Bạn vừa nhập: "+value.get())
        said.grid(column=0, row=1, pady=20, columnspan=5)

##Attributes--------------------------------------------------------------#
#icon
green = tk.PhotoImage(file= r"icon/green.png")
red = tk.PhotoImage(file = r"icon/red.png")
blue = tk.PhotoImage(file = r"icon/blue.png")
#Green Button
text = tk.Button(ass, \
    text="Text",       \
    image=green,        \
    compound="center",   \
    foreground="white",   \
    command=noVoice)
text.grid(column=0, row=0, padx=5)
#Red Button 
voice = tk.Button(ass, \
    text="Voice",       \
    image=red,           \
    compound="center",    \
    foreground="white",    \
    command=ask)        
voice.grid(column=1, row=0, padx=5)

#TypeText---------------------------------------------------#
value = tk.StringVar()
entry = tk.Entry(ass, textvariable=value, width=10)
action = tk.Button(ass, text="OK", command=typeText)

#Result - What you just said
said = tk.Label(wraplength=200)
ass.mainloop()
#end

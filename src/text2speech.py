from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text, lang='vi')
    tts.save("tmp.mp3")
    os.system("mpg321 tmp.mp3")
    os.system("rm -rf tmp.mp3")
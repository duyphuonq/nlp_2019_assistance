from gtts import gTTS
import os
tts = gTTS(text='Xin chào buổi sáng, chúc phương một ngày tốt lành', lang='vi')
tts.save('good.mp3')
os.system('mpg321 good.mp3')
os.system('rm -rf good.mp3')


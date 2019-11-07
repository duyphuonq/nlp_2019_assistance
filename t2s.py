from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('chúc phương một ngày tốt lành', 'vi')
tts.write_to_fp(mp3_fp)

from gtts import gTTS
import os

text = "Hello world"
file = "salida.mp3"
tts = gTTS(text, lang='en')
tts.save(file)
os.system(file)

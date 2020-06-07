from gtts import gTTS
import os

texto="Hello world"
file = "salida.mp3"
tts = gTTS(texto, 'es')
tts.save(file)
os.system("mpg123 " + file)
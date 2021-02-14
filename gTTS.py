from gtts import gTTS
import playsound

def speaker(text):
     tts = gTTS(text = text, lang = 'en')
     filename = 'voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)

speaker('hello world')
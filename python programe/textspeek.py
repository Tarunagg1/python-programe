from gtts import gTTs
import os
f = open('speak.txt')
x = f.read();

language = 'en'
audio=  gTTs(text=x,Lang=language,slow=False)
audio.save('1.wav')
os.system('1.wav');
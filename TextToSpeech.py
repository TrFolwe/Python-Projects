from gtts import gTTS
from playsound import playsound

data = {"1234": "Ülker çikolatalı gofret 1.50 TL"}
id = "1234";
mytext = data[id]
language = "tr"

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("sound.mp3")
print("Sound is saved")
playsound("sound.mp3")
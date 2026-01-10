import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
engine.setProperty('volume', 0.5)  # Range: 0.0 – 1.0

voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty('voice', voices[1].id)


engine.say("Hello, welcome to text to speech learning")
engine.runAndWait()

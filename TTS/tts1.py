import pyttsx3

engine = pyttsx3.init()

# rate = engine.getProperty('rate')
engine.setProperty('rate', 150)   # (Slow: 100–150) (Normal: 180–220) (Fast: 250–300)
engine.setProperty('volume', 1.0)  # Range: 0.0 – 1.0

voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty('voice', voices[1].id)


engine.say("Hello, welcome to text to speech learning")
engine.runAndWait()

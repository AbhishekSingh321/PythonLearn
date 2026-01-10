from gtts import gTTS


#Hello, welcome to online text to speech learning

text = "Hola, bienvenido al aprendizaje en línea de texto a voz"  
tts = gTTS(text=text, lang='es',slow=True)  #Effect=> slow : True(slow),False(normal)

tts.save("voice_tts2.mp3")
print("Audio saved as voice_tts2.mp3")



# gTTS("Hello", lang="en")     # English
# gTTS("नमस्ते", lang="hi")    # Hindi
# gTTS("Bonjour", lang="fr")   # French
# gTTS("Hola", lang="es")      # Spanish

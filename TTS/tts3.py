import asyncio
import edge_tts

async def main():
    text="Hello, welcome to text to speech learning"
    voice = "en-US-BrianNeural"    #edge-tts --list-voices


    #(rate "+10%","-20%")   (pitch	"+10Hz","-5Hz")  (volume	"+0%","+50%")
    communicate = edge_tts.Communicate(text=text,voice=voice,rate="+10%",pitch="+0Hz",volume="+50%")

    await communicate.save("voice_tts3.mp3")  #,"subtitle_tts3.srt")

asyncio.run(main())

#---------------------------Mine top Best Voices--------------------------------------------
# 1.en-GB-SoniaNeural
# 2.en-US-EmmaMultilingualNeural
# 3.en-US-BrianNeural
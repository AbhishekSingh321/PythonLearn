from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
import os

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

text='''Hello, welcome to text to speech learning,
         I’m Abhishek Singh. I enjoy learning, building things, and improving a little every day. I like solving problems and keeping things simple and practical.
    '''

audio = client.text_to_speech.convert(
    text=text,
    voice_id="gJvkwI7wGFW2czmyfJhp",    # Use any voice from elevenLab with thier voiceID
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

with open("voice_tts4.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)


# play(audio)
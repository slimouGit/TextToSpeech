from pathlib import Path
from openai import OpenAI

from config import API_KEY

client = OpenAI(api_key=API_KEY)

def textToSpeech():
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Hello world! This is a streaming test.",
    )

    with open("output.mp3", "wb") as out_file:
        out_file.write(response.read())

if __name__ == '__main__':
    textToSpeech()
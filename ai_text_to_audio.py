
from pathlib import Path
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
)
# Ensure the API key is set
if client.api_key is None:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")


# Define the path for the output audio file
speech_file_path = Path(__file__).parent / "speech1.mp3"

# Create the audio content using OpenAI's TTS
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="WORLD WAR II was a scientific war: its outcome was determined largely by the effective  deployment  of  scientific  research  and  technical  developments.  The  best known wartime scientific program was the Manhattan Project at Los Alamos to develop the atomic bomb. Another major program of the same scale and importance"
)

# Write the audio content to the file
with open(speech_file_path, "wb") as f:
    f.write(response.content)


p
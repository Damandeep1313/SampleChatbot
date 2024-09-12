import os
from groq import Groq

# Initialize the Groq client with the API key
api_key = "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"
client = Groq(api_key=api_key)

# Specify the path to the audio file
filename = "record.wav"

def transcribe_audio():
    if not os.path.exists(filename):
        print(f"Audio file '{filename}' not found.")
        return

    print(f"Transcribing {filename} using Groq Whisper...")

    try:
        # Open the audio file and make the transcription request
        with open(filename, "rb") as file:
            transcription = client.transcriptions.create(
                file=(filename, file.read()),  # Required audio file
                model="distil-whisper-large-v3-en",  # Ensure this is the correct model name
                prompt="Specify context or spelling",  # Optional
                response_format="json",  # Optional
                language="en",  # Optional
                temperature=0.0  # Optional
            )

        # Write the transcription to a file
        with open("transcription.txt", "w") as text_file:
            text_file.write(transcription['text'])

        print("Transcription has been saved to transcription.txt")

    except AttributeError as e:
        print(f"API method not found: {e}")
    except Exception as e:
        print(f"An error occurred during transcription: {e}")

if __name__ == "__main__":
    transcribe_audio()

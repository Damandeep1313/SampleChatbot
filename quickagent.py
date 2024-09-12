import os
import time
import subprocess

def run_quick_agent():
    print("Waiting for 'record.wav' to be available...")

    # Wait until the record.mp3 file is created
    while not os.path.exists('record.wav'):
        time.sleep(1)

    print("File 'record.mp3' found, running transcription script...")
    # Call the transcription script
    subprocess.run(['python', 'transcribe.py'])

if __name__ == "__main__":
    print("Starting audio recording and agent...")
    subprocess.run(['python', 'record.py'])  # Record audio
    run_quick_agent()  # Wait for the audio file and transcribe it


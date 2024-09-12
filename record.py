import sounddevice as sd
import numpy as np
import wavio
from pydub import AudioSegment

# Parameters
duration = 10  # seconds
sample_rate = 44100  # Sample rate (Hz)
output_wav_file = 'record.wav'
output_mp3_file = 'record.mp3'

def record_audio():
    print("Recording audio...")
    # Record audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is done

    # Save as a WAV file
    wavio.write(output_wav_file, recording, sample_rate, sampwidth=2)

    # Convert WAV to MP3
    print(f"Converting {output_wav_file} to MP3...")
    sound = AudioSegment.from_wav(output_wav_file)
    
    print(f"Audio recorded and saved as {output_mp3_file}.")

if __name__ == "__main__":
    record_audio()

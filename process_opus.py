# scripts/process_opus.py
import speech_recognition as sr
from pydub import AudioSegment
import os
import sys

file_path = sys.argv[1]
# Konversi file MP3 ke WAV
audio = AudioSegment.from_mp3(file_path)
audio.export("audio.wav", format="wav")

# Inisialisasi recognizer
recognizer = sr.Recognizer()

# Buka file WAV
with sr.AudioFile("audio.wav") as source:
    # Rekam audio dari file
    audio_data = recognizer.record(source)
    try:
        # Lakukan speech recognition
        text = recognizer.recognize_google(audio_data, language="id-ID")
        print(text)
    except sr.UnknownValueError:
        print("tidak mengenali audio")
    except sr.RequestError as e:
        print("Error :", e)
    
# Hapus file WAV setelah selesai
os.remove("audio.wav")

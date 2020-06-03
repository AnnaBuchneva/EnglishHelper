import os
import copy
import random
import pyttsx3
import googletrans
import spellchecker
import difflib
import re
import pyaudio
import speech_recognition


def record():
    # source: https://stackabuse.com/introduction-to-speech-recognition-with-python/
    mic = speech_recognition.Microphone()
    with mic as audio_file:
        print("Speak Please")
        speech_recognition.Recognizer.adjust_for_ambient_noise(audio_file)
        audio = speech_recognition.Recognizer.listen(audio_file)
        print("Converting Speech to Text...")
        print("You said: " + speech_recognition.Recognizer.recognize_google(audio))



record()

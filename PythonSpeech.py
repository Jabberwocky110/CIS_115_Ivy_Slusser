import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
  print("What do you want to say?")
  r = sr.Recognizer()
  Speech = r.listen(source)
  Text = (Speech)
  Input = input(Text)
  RecognizedSpeech = r.recognize_google(Input)
import os
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"
from google import genai
client = genai.Client()


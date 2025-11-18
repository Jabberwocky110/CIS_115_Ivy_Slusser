import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
  print("What do you want to say?")
  Speech = r.listen(source)
  Text = r.recognize_google(Speech)

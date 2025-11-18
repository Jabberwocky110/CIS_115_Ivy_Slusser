import speech_recognition as sr
r = sr.Recognizer()
def speechrecognition():
    print("What do you want to say?")
    with sr.Microphone as source:
      Speech = r.listen(source)
      Text = r.recognize_google(Speech)
speechrecognition()
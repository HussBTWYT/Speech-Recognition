import speech_recognition as sr # Libary for Speech Recognition Data System

r = sr.Recognizer()

with sr.AudioFile("audio.wav") as source:
    audio = r.listen(source) # sr.AudioFile("audio.wav")
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Failed to produce text from the source audio, try again.")

# SPEECHRECOGNITION.PY

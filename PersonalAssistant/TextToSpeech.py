import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 130)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # index 1 is for female voice


def get_audio(text):
    engine.say(text)
    engine.runAndWait()

get_audio("Hi Lasritha, i love you, Have a bright future")



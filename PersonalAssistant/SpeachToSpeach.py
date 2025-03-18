import multiprocessing
import pyttsx3
import keyboard
import speech_recognition

UserVoiceRecognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speechtotext():
        
    try:
        with speech_recognition.Microphone() as Source:
            UserVoiceInput = UserVoiceRecognizer.listen(Source)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput).lower()
        return UserVoiceInput_converted_to_Text           
    
    except speech_recognition.UnknownValueError:
        return "No user voice"

def sayFunc(phrase):
    engine.say(phrase)
    engine.runAndWait()

def say(phrase):
	p = multiprocessing.Process(target=sayFunc, args=(phrase,))
	p.start()
	while p.is_alive():
		if keyboard.is_pressed('q'):
			p.terminate()
		else:
			continue
	p.join()


if __name__ == "__main__":
	while 1:
		text = speechtotext()
		say(text)
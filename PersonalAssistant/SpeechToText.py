import speech_recognition


def speechtotext():
    UserVoiceRecognizer = speech_recognition.Recognizer()
    
    try:
        with speech_recognition.Microphone() as Source:
            UserVoiceInput = UserVoiceRecognizer.listen(Source)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput).lower()
        return UserVoiceInput_converted_to_Text           
    
    except speech_recognition.UnknownValueError:
        return "No user voice"

#print(speechtotext())  
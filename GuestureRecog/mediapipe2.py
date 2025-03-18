# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time

import pyttsx3  # For text to speech
engine = pyttsx3.init()

# STEP 2: Create an GestureRecognizer object.
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

map = {"None":"None", "Closed_Fist":"Stop the engine", "Open_Palm":"Start the engine", "Thumb_Down":"Moving Backward", "Thumb_Up":"Moving Forward", "Pointing_Up":"Turning Left", "Victory":"Turning Right", "ILoveYou":"Sounding Horn"}

last_gesture = "None"
vid = cv2.VideoCapture(0) 
while(True): 
	
	ret, frame = vid.read() 
	cv2.imshow('frame', frame)
	cv2.imwrite("image.jpg", frame)

	# STEP 3: Load the input image.
	image = mp.Image.create_from_file("image.jpg")

	# STEP 4: Recognize gestures in the input image.
	recognition_result = recognizer.recognize(image)

	# STEP 5: Display the reult
	if len(recognition_result.gestures) != 0:
		gesture = recognition_result.gestures[0][0].category_name
		if gesture != last_gesture and gesture != "None":
		    print(map[gesture])
		    engine.say(map[gesture])
		    engine.runAndWait()
		    last_gesture = gesture
		

	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break
 

vid.release() 
cv2.destroyAllWindows() 
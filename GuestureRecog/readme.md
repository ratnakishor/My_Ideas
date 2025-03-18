# Hand Gesture Based Announcement System

It is a system to announce various instructions based on hand gestures using mediapipe library model.

Install dependencies using *pip install -r requirements.txt*.

Change the following mapping dictionary statement in the code to assign different tasks (function calls) to various hand gestures supported by mediapipe model.  

map = {"None":"None", "Closed_Fist":"Stop the engine", "Open_Palm":"Start the engine", "Thumb_Down":"Moving Backward", "Thumb_Up":"Moving Forward", "Pointing_Up":"Turning Left", "Victory":"Turning Right", "ILoveYou":"Sounding Horn"}
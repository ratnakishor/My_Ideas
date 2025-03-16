import cv2
from ultralytics import YOLO
import pywhatkit

def send_message(to, image):
    pywhatkit.sendwhats_image(to, image, "Cell Phone Detected")

def get_classes():
    videoCap = cv2.VideoCapture(0)
    ret, frame = videoCap.read()
    while not ret:
        continue
    results = yolo.track(frame, stream=True)
    

    for result in results:
        # get the classes names
        classes_names = result.names

        #Predicted class names
        classes = []

        # iterate over each box
        for box in result.boxes:
                # get the class
                cls = int(box.cls[0])

                # get the class name
                class_name = classes_names[cls]
                classes.append(class_name)
    return (frame, classes)
    
    
    

# Load the model
#yolo = YOLO('yolov8s.pt')
yolo = YOLO('yolov5s.pt') 

# Load the video capture
videoCap = cv2.VideoCapture(0)

while True:

    frame, classes = get_classes()
                              
    # show the image
    cv2.imshow('frame', frame)
    if "cell phone" in classes:
        print("Cell Phone detected")
        cv2.imwrite("image.jpg", frame)
        send_message("+91 8328373501", "image.jpg")
    while "cell phone" in get_classes()[1]:
        pass
        
    # break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture and destroy all windows
videoCap.release()
cv2.destroyAllWindows()

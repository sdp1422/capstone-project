# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

rawCapture = PiRGBArray(camera, size=(640, 480))

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, one face id
face_id = 1

# Initialize sample face image
count = 0

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image_frame = frame.array
	
	# Convert frame to grayscale
	gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
	
	# Detect frames of different sizes, list of faces rectangles
	faces = face_detector.detectMultiScale(gray, 1.3, 5)
	
	#Loops for each faces
	
	for (x,y,w,h) in faces:
		
		# Crop the image frame into rectangle
		cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
		
		# Increment sample face image
		count += 1
		
		# Save the captured image into the datasets folder
		cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
		
		# Display the video frame, with bounded rectangle on the peerson's face
		cv2.imshow('frame', image_frame)
	
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# If image taken reach 100, stop taking video
	elif count>100:
            break

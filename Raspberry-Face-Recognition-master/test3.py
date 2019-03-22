# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

face_id = 2

count = 0
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# faces = faceCascade.detectMultiScale(gray,1.3,5)
	
	print ("Found "+str(len(faces))+" face(s)")
	
	for (x,y,w,h) in faces:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		count += 1

		cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])

	# show the frame
	cv2.imshow("Frame", image)
	# cv2.imwrite('result.jpg',image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	if count>100:
		break

#-*-coding:utf-8-*-
# Import OpenCV2 for image processing
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import subprocess
from firebase import firebase

# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
# recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face_LBPHFaceRecognizer.create()

firebase = firebase.FirebaseApplication('https://kbms-bot.firebaseio.com/')

# Load the trained mode
# recognizer.load('trainer/trainer.yml')
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
face_cascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
# cam = cv2.VideoCapture(0)
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera,size=(640,480))

time.sleep(0.1)

isSdpUp = False
isWgUp = False

# Loop
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

	# Read the video frame
	# ret, im =cam.read()
	image = frame.array

	# Convert the captured frame into grayscale
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	# Get all face from the video frame
	# faces = faceCascade.detectMultiScale(gray, 1.2,5)
	faces = face_cascade.detectMultiScale(gray, 1.2,5)

	# For each face in faces
	for(x,y,w,h) in faces:

		# Create rectangle around the face
		cv2.rectangle(image, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

		# Id = (0, 0)

		# Recognize the face belongs to which ID
		Id = recognizer.predict(gray[y:y+h,x:x+w])
		
		accuracy = Id[1]
		# aaa = Id[1:2]
		# Id = ''.join(Id)
		Id = Id[0]
		# Check the ID if exist
		if(Id == 1):
			if accuracy <= 150:
				Id = "SangDonPark"
				msgText = ''
				childNum = firebase.get('/childNum/number',None)
				isBusUp = firebase.get('/childIsBusUp/I4UeW6sbCBUWF4ZlYIpDcBdorhq2',None)
				if(isSdpUp == False):
					cmd = 'node /home/pi/Documents/nodejs/fcm_test1_sdp_up.js'
					isSdpUp = True
					msgText = '박상돈님이 승차하였습니다.'
					childNum = childNum+1
					isBusUp = '승차'
				else:
					cmd = 'node /home/pi/Documents/nodejs/fcm_test1_sdp_down.js'
					isSdpUp = False
					msgText = '박상돈님이 하차하였습니다.'
					childNum = childNum-1
					isBusUp = '하차'
				subprocess.call(cmd,shell=True)
				now = time.localtime()
				timeNow = "%02d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                                timeNow = (str)((int)(time.time()*1000))
                                result = firebase.post('/chatmodel/I4UeW6sbCBUWF4ZlYIpDcBdorhq2',{'message':msgText,'timeStamp':timeNow, 'userModel': {'name': 'bot','photo_profile':'https://lh5.googleusercontent.com/-t-AkPxrxMCY/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rdCRC4c6be0iIimK1BniTfkSkvGYQ/s96-c/photo.jpg'}})
				firebase.put('childNum','number',childNum)
				firebase.put('childIsBusUp','I4UeW6sbCBUWF4ZlYIpDcBdorhq2',isBusUp)
				time.sleep(3)
			else:
				Id = "Unknow"
			# cv2.putText(image, str(Id), (x,y-40), font, 2, (255,255,255), 3)
		#If not exist, then it is Unknown
		elif(Id == 2):
              		if accuracy <= 150:
				Id = "ArseneWenger"
				msgText = ''
				childNum = firebase.get('/childNum/number',None)
				isBusUp = firebase.get('/childIsBusUp/HxYcAOS8lJYQxeWxxMXoKqV4V7m2',None)
				if(isWgUp == False):
					cmd = 'node /home/pi/Documents/nodejs/fcm_test1_wg_up.js'
					isWgUp = True
					msgText = '벵거님이 승차하였습니다.'
					childNum = childNum+1
					isBusUp = 'ArseneWenger is up.'
                                        print('arsene is up.')
				else:
					cmd = 'node /home/pi/Documents/nodejs/fcm_test1_wg_down.js'
					isWgUp = False
					msgText = '벵거님이 하차하였습니다.'
					childNum = childNum-1
					isBusUp = 'ArseneWenger is down.'
                                        print('arsene is down.')
				subprocess.call(cmd,shell=True)
				now = time.localtime()
				timeNow = "%02d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                                timeNow = (str)((int)(time.time()*1000))
                                result = firebase.post('/chatmodel/HxYcAOS8lJYQxeWxxMXoKqV4V7m2',{'message':msgText,'timeStamp':timeNow, 'userModel':{'name':'bot', 'photo_profile':'https://lh5.googleusercontent.com/-t-AkPxrxMCY/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rdCRC4c6be0iIimK1BniTfkSkvGYQ/s96-c/photo.jpg'}})
				firebase.put('childNum','number',childNum)
				firebase.put('childIsBusUp','HxYcAOS8lJYQxeWxxMXoKqV4V7m2',isBusUp)
				time.sleep(3)
			else:
				Id = "Unknow"
			# cv2.putText(image, str(Id), (x,y-40), font, 2, (255,255,255), 3)
		else:
			print (Id)
			# print (type(Id))
			Id = "Unknow"
			# cv2.putText(image, str(Id), (x,y-40), font, 2, (255,255,255), 3)

		# Put text describe who is in the picture
		cv2.rectangle(image, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
		cv2.putText(image, str(Id), (x,y-40), font, 2, (255,255,255), 3)

	# Display the video frame with the bounded rectangle
        
        
        # sangdon's message : this is lag.
        # cv2.imshow('image',image)

	rawCapture.truncate(0)

	# If 'q' is pressed, close program
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

# Stop the camera
# cam.release()

# Close all windows
# cv2.destroyAllWindows()

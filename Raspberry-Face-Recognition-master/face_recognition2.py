#-*-coding:utf-8-*-
# Import OpenCV2 for image processing
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import subprocess
from firebase import firebase
from pyfcm import FCMNotification

# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
# recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face_LBPHFaceRecognizer.create()
# recognizer = cv2.face.LBPHFaceRecognizer_create()

firebase = firebase.FirebaseApplication('https://kbms-bot.firebaseio.com/')

# Load the trained mode
# recognizer.load('trainer/trainer.yml')
recognizer.read('trainer/trainer.yml')
# recognizer.read('trainer/trainer.yml')

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

user_name = []
user_name.append('user none')
user_name.append('sdp14222')
user_name.append('sdp1422j')

user_uid = []
user_uid.append('user uid none')
user_uid.append('I4UeW6sbCBUWF4ZlYIpDcBdorhq2')
user_uid.append('tdANSqXd5IV87HN2SCr9VBBb62I3')

user_is_up = []
user_is_up.append(True)
user_is_up.append(False)
user_is_up.append(False)

api_key = "AAAAyW2dkpk:APA91bHWFYE4xIDX9JOWix6SKukgeH-AWfTrBe9b3G-XNO-9V0uNc-L6ngEQ929HEFB1r1G_KBbagdVSR895cMOg3KErvJR_jG7yQvVu5w1rr310u6ynyi_dg7CSYNtpgrh82q5hJhin"

push_service = FCMNotification(api_key=api_key)

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
		id, accuracy = recognizer.predict(gray[y:y+h,x:x+w])
		
		size = len(user_name)
		for i in range(1, size + 1):
                    if i == id and accuracy <= 150:
                        user_is_up[i] = not user_is_up[i]
                        childNum = firebase.get('/childNum/number',None)
                        isBusUp = firebase.get('/childIsBusUp/'+ str(user_is_up[i]),None)
                        isBusUp = str(user_is_up[i])
                        
                        msgIsUp = ''
                        if user_is_up[i]:
                            childNum += 1
                            msgIsUp = 'up'    
                        else:
                            childNum -= 1
                            msgIsUp = 'down'
                        
                        msgText = ''
                        msgText += str(user_name[i]) + ' is bus ' + msgIsUp
                        timeStamp = str(int(time.time()))
                        print('user_name = ' + str(user_name[i]))
                        print('user_uid = ' + str(user_uid[i]))
                        print('user_is_up = ' + str(user_is_up[i]))
                        print('childNum = ' + str(childNum))
                        print('isBusUp = ' + str(isBusUp))
                        print('msgText = ' + msgText)
                        
                        
                        userModel = {
                            'name': 'sangdon park',
                            'photo_profile': 'https://lh5.googleusercontent.com/-t-AkPxrxMCY/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rdCRC4c6be0iIimK1BniTfkSkvGYQ/s96-c/photo.jpg'
                        }
                        
                        result = firebase.post('/chatmodel/' + str(user_uid[i]), {'message': msgText, 'timeStamp': timeStamp, 'userModel': userModel})
                        firebase.put('childNum','number',childNum)
                        firebase.put('childIsBusUp', str(user_uid[i]), str(user_is_up[i]))
                        
                        registration_id = "e32Gvxx090M:APA91bGA8LLICfvLdbRP-fvm7ga5Yb7Sv8Xia0kp_ocjLCaldu5v1prSr5FlTqyC722QCWFJK4YNDIvsNAPSViWYBjdaEPcN8PpUaEojPKEeCXOlqKC3GojhoD3Mcl8gMCemj5_X8wWq"
                        message_title = "Hahahaha"
                        message_body = "Hi john, your customized news for today is ready"
                        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

		# Put text describe who is in the picture
		cv2.rectangle(image, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
		# cv2.putText(image, str(Id), (x,y-40), font, 2, (255,255,255), 3)

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

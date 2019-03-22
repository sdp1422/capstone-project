from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.capture('example.jpg')
# time.sleep(3)

img = cv2.imread('example.jpg',0)

cv2.imshow("Frame", img)

k=cv2.waitKey(0) & 0xFF
# if k=='q'
import cv2
import time

fname = 'example.jpg'

img = cv2.imread(fname, 1)
# time.sleep(1)
cv2.imshow('FRAME', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
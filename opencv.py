import numpy as np
import cv2

cap = cv2.VideoCapture('test.mov')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    if i % 60 == 0:
	    cv2.imwrite("frame" + str(i) + ".png",frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
    i = i + 1

cap.release()
cv2.destroyAllWindows()

# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# cv2.imshow('frame',gray)

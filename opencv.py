import numpy as np
import cv2

cap = cv2.VideoCapture('test.mov')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    if frame == None:
    	break

    if i % 60 == 0:
	    cv2.imwrite("frame" + str(i) + ".png",frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
    i = i + 1

cap.release()
# cv2.destroyAllWindows()
import numpy as np
import cv2
import clarifai

cap = cv2.VideoCapture('test.mov')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    if frame == None:
    	break

    # todo: get number of frames per second
    if i % 60 == 0:
		height, width = frame.shape[:2]
		if width > 1024:
			# print width
			scale = 1024 / float(width)
			# print scale
			img = cv2.resize(frame,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
			# print img.shape[:2]
		else:
			img = frame
		filename = "frame" + str(i) + ".png"
		cv2.imwrite(filename, img)
		print clarifai.get_tags_from_file(filename)

    i = i + 1

cap.release()
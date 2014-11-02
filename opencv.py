import numpy as np
import uuid
import cv2
from cv2.cv import CV_CAP_PROP_FPS, CV_CAP_PROP_POS_MSEC
import clarifai

def extract_tags(filename, interval=10):
	""" Return the tags in the movie in filename
	interval -- interval between frames in seconds
	"""
	cap = cv2.VideoCapture(filename)
	FPS = cap.get(CV_CAP_PROP_FPS)
	frame_interval = int(round(interval * FPS))
	imgs = []
	ten_mins = int(round(FPS))*60*10
	img_name = str(uuid.uuid1()) + ".png"
	i = 0
	while (cap.isOpened()):
		ret, frame = cap.read()
		if frame is None:
			break
		if i % frame_interval == 0:
			t = cap.get(CV_CAP_PROP_POS_MSEC)
			if (int(round(t * 1000*60))) == 0:
				print cap.get(CV_CAP_PROP_POS_MSEC) + ' mins'
			height, width = frame.shape[:2]
			if width > 1024:
				scale = 1024 / float(width)
				img = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
			else:
				img = frame
			cv2.imwrite(img_name, img)
			try:
				tags = clarifai.get_tags_from_file(img_name)
				imgs.append(tags)
			except:
				continue

		i += 1

	cap.release()
	return imgs

def create_movie(argv):
	import models
	images = extract_tags(argv[1], int(argv[2]))
	movie = models.Movie(name=argv[0], imgs=images).save()

import sys
if __name__ == "__main__":
   create_movie(sys.argv[1:])
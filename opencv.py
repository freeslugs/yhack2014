import numpy as np
import cv2
import clarifai


def extract_tags(filename, interval=2, FPS=30):
	""" Return the tags in the movie in filename
	interval -- interval between frames in seconds
	FPS -- frame per second
	"""
	cap = cv2.VideoCapture(filename)
	frame_interval = interval * FPS
	frames = []

	i = 0
	while (cap.isOpened()):
		ret, frame = cap.read()
		if frame is None:
			break
		if i % frame_interval == 0:
			height, width = frame.shape[:2]
			if width > 1024:
				# print width
				scale = 1024 / float(width)
				# print scale
				img = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
				# print img.shape[:2]
			else:
				img = frame
			img_name = "frame" + str(i) + ".png"
			cv2.imwrite(img_name, img)
			tags = clarifai.get_tags_from_file(img_name)
			tags['frame'] = i

			frames.append(tags)

		i += 1

	cap.release()
	return frames

print extract_tags('test.mov')
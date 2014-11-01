import cv2
import numpy

vidcap = cv2.VideoCapture('smalltest.mp4')

success,image = vidcap.read()

print success

count = 0;
while success:
  print count
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1

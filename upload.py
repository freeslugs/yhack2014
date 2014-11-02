import opencv
import models

def upload(name, filename, interval):

	try:
		images = opencv.extract_tags(filename, interval)
		movie = models.Movie(name=name, imgs=opencv.extract_tags(filename, interval)).save()
		return movie.imgs
	except Exception, e:
		return {'error': str(e)}


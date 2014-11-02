import models 
import sys

def add_movie(name, filename): 
	try:
		print "get movie"
		movie = models.Movie.objects.get(name=name)
	except KeyError, e:
		error = e.message + ' not specified'
		return {"error": error}
	except models.Movie.DoesNotExist:
		import opencv
		print "get images"
		interval = 10
		images = opencv.extract_tags(filename, interval)
		movie = models.Movie(name=name, imgs=images)
		return movie.imgs	
	return {"error": "Movie already exists"}

print sys.argv[1], sys.argv[2]
print add_movie(sys.argv[1], sys.argv[2])
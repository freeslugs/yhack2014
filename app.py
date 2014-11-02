#!/usr/bin/env python

from flask import Flask, request
from flask.ext import restful
from flask.ext.mongoengine import MongoEngine
from mongoengine import *
from flask.ext.cors import CORS, cross_origin
import models #import Movie, Image
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)
cors = CORS(app)

app.debug = True
app.config["MONGODB_SETTINGS"] = {'DB': "yhacks"}
connect('yhacks', host='mongodb://admin:columbia@ds047940.mongolab.com:47940/yhacks')
# connect('yhacks')

api = restful.Api(app)

db = MongoEngine(app)

#def get_imgs_from_list(l):
#	for img in l:
#		img = Image(tag=img.tag,)

@app.route("/")
def index():
	return app.send_static_file("index.html")


class GetMovie(restful.Resource):
	def get(self):
		try:
			name = request.args['name']
		except:
			return {"error": "Missing name of movie."}
		try:
			import analyze
			imgs = models.Movie.objects.get(name=name).imgs
			return analyze.remove_outliers(imgs)
		except models.Movie.DoesNotExist:
			return {"error": "Movie was not found."}

class AddMovie(restful.Resource):
	def post(self):
		try:
			data = request.json
			name = data['name']
			filename = data['filename']
			interval = data['interval']
			movie = models.Movie.objects.get(name=name)
		except KeyError, e:
			error = e.message + ' not specified'
			return {"error": error}
		except models.Movie.DoesNotExist:
			import opencv
			try:
				images = opencv.extract_tags(filename, interval)
				movie = models.Movie(name=name, imgs=opencv.extract_tags(filename, interval)).save()
				return movie.imgs
			except Exception, e:
				return {'error': str(e)}
		return {"error": "Movie already exists"}

class MovieList(restful.Resource):
	def get(self):
		names = []
		movies =  models.Movie.objects()
		for movie in movies:
			names.append(movie.name)
		return names

api.add_resource(GetMovie, "/api/get-movie")
api.add_resource(AddMovie, "/api/add-movie")
api.add_resource(MovieList, "/api/movie-list")

if __name__ == "__main__":
	app.run()

#!/usr/bin/env python

from flask import Flask, request, redirect, url_for, send_from_directory
from flask.ext import restful
from flask.ext.mongoengine import MongoEngine
from mongoengine import *
from flask.ext.cors import CORS, cross_origin
import models #import Movie, Image
from werkzeug.exceptions import BadRequestKeyError
import os
from werkzeug import secure_filename
import requests
import json
app = Flask(__name__)
cors = CORS(app)


server_url = "localhost:5000"
# server_url = "mooview.ngrok.com"


UPLOAD_FOLDER = './movies'
ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mov'])

# app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.debug = True
app.config["MONGODB_SETTINGS"] = {'DB': "yhacks"}
connect('yhacks', host='mongodb://admin:columbia@ds047940.mongolab.com:47940/yhacks')
# connect('yhacks')

api = restful.Api(app)

db = MongoEngine(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                import upload
                print request.form['name']
                print filename
                upload.upload(request.form['name'], os.path.join(app.config['UPLOAD_FOLDER'], filename), 2)
                return redirect(server_url + "/?notice=upload-success")
			#url = "http://localhost:8080/api/add-movie"
			#data = { 'name': request.form['name'], 'filename': filename, 'interval': 10, 'upload': True }
			#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			#return requests.post(url, data=json.dumps(data), headers=headers)
			#return "success"
    return app.send_static_file("index.html")

@app.route('/movies/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
			import upload
			upload.upload(name, filename, interval)
			return {"Success": "Request submitted"}
		return {"error": "Movie already exists"}

class MovieList(restful.Resource):
	def get(self):
		names = []
		movies =  models.Movie.objects()
		for movie in movies:
			names.append(movie.name)
		return names
  
class Tags(restful.Resource):
    def get(self):
        tag = request.args.get('tag', '')
        import analyze
        return analyze.get_tag(tag)

api.add_resource(GetMovie, "/api/get-movie")
api.add_resource(AddMovie, "/api/add-movie")
api.add_resource(MovieList, "/api/movie-list")
api.add_resource(Tags, "/api/tags")

if __name__ == "__main__":
	app.run()

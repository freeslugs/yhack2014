#!/usr/bin/env python
from flask import Flask
from flask.ext import restful
from flask.ext.mongoengine import *
from mongoengine import *


app = Flask(__name__)
api = restful.Api(app)
app.debug = True

app.config.from_pyfile('settings.py')

db = MongoEngine(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")

class MovieTags(restful.Resource):
	def get(self):
		return [{
		  'boy': 0.0086517333984375,
		  'eyes': 0.0077972412109375,
		  'fashion': 0.0270538330078125,
		  'facial expression': 0.00783538818359375, 
		  'music': 0.00846099853515625, 
		  'browse': 0.00992584228515625,
		  'light': 0.00835418701171875,
		  'wealthy': 0.00717926025390625,
		  'men': 0.00981903076171875,
		  'smoke': 0.006793975830078125,
		  'face': 0.0162506103515625,
		  'woman': 0.01036834716796875,
		  'studio': 0.01097869873046875,
		  'female': 0.00852203369140625,
		  'pineapple': 0.0196990966796875,
		  'portrait': 0.135498046875,
		  'model': 0.037933349609375,
		  'girl': 0.01322174072265625,
		  'black and white': 0.01206207275390625,
		  'man': 0.011138916015625
		  },
		{
		 'boy': 0.007747650146484375,
		 'eyes': 0.0124664306640625,
		 'fashion': 0.0369873046875,
		 'kids': 0.005706787109375,
		 'learning': 0.006931304931640625,
		 'sitting': 0.006256103515625,
		 'browse': 0.00951385498046875,
		 'light': 0.007724761962890625,
		 'colour': 0.006313323974609375,
		 'children': 0.00666046142578125,
		 'face': 0.0149078369140625,
		 'hair': 0.0072021484375,
		 'woman': 0.01548004150390625,
		 'studio': 0.01544952392578125,
		 'smile': 0.0057220458984375,
		 'female': 0.00919342041015625,
		 'pineapple': 0.0216217041015625,
		 'portrait': 0.112060546875,
		 'model': 0.059783935546875,
		 'girl': 0.0238037109375
		 },
		 {
		  'boy': 0.0086517333984375,
		  'eyes': 0.0077972412109375,
		  'fashion': 0.0270538330078125,
		  'facial expression': 0.00783538818359375, 
		  'music': 0.00846099853515625, 
		  'browse': 0.00992584228515625,
		  'light': 0.00835418701171875,
		  'wealthy': 0.00717926025390625,
		  'men': 0.00981903076171875,
		  'smoke': 0.006793975830078125,
		  'face': 0.0162506103515625,
		  'woman': 0.01036834716796875,
		  'studio': 0.01097869873046875,
		  'female': 0.00852203369140625,
		  'pineapple': 0.0196990966796875,
		  'portrait': 0.135498046875,
		  'model': 0.037933349609375,
		  'girl': 0.01322174072265625,
		  'black and white': 0.01206207275390625,
		  'man': 0.011138916015625
		  },
		{
		 'boy': 0.007747650146484375,
		 'eyes': 0.0124664306640625,
		 'fashion': 0.0369873046875,
		 'kids': 0.005706787109375,
		 'learning': 0.006931304931640625,
		 'sitting': 0.006256103515625,
		 'browse': 0.00951385498046875,
		 'light': 0.007724761962890625,
		 'colour': 0.006313323974609375,
		 'children': 0.00666046142578125,
		 'face': 0.0149078369140625,
		 'hair': 0.0072021484375,
		 'woman': 0.01548004150390625,
		 'studio': 0.01544952392578125,
		 'smile': 0.0057220458984375,
		 'female': 0.00919342041015625,
		 'pineapple': 0.0216217041015625,
		 'portrait': 0.112060546875,
		 'model': 0.059783935546875,
		 'girl': 0.0238037109375
		 },
		 {
		  'boy': 0.0086517333984375,
		  'eyes': 0.0077972412109375,
		  'fashion': 0.0270538330078125,
		  'facial expression': 0.00783538818359375, 
		  'music': 0.00846099853515625, 
		  'browse': 0.00992584228515625,
		  'light': 0.00835418701171875,
		  'wealthy': 0.00717926025390625,
		  'men': 0.00981903076171875,
		  'smoke': 0.006793975830078125,
		  'face': 0.0162506103515625,
		  'woman': 0.01036834716796875,
		  'studio': 0.01097869873046875,
		  'female': 0.00852203369140625,
		  'pineapple': 0.0196990966796875,
		  'portrait': 0.135498046875,
		  'model': 0.037933349609375,
		  'girl': 0.01322174072265625,
		  'black and white': 0.01206207275390625,
		  'man': 0.011138916015625
		  },
		{
		 'boy': 0.007747650146484375,
		 'eyes': 0.0124664306640625,
		 'fashion': 0.0369873046875,
		 'kids': 0.005706787109375,
		 'learning': 0.006931304931640625,
		 'sitting': 0.006256103515625,
		 'browse': 0.00951385498046875,
		 'light': 0.007724761962890625,
		 'colour': 0.006313323974609375,
		 'children': 0.00666046142578125,
		 'face': 0.0149078369140625,
		 'hair': 0.0072021484375,
		 'woman': 0.01548004150390625,
		 'studio': 0.01544952392578125,
		 'smile': 0.0057220458984375,
		 'female': 0.00919342041015625,
		 'pineapple': 0.0216217041015625,
		 'portrait': 0.112060546875,
		 'model': 0.059783935546875,
		 'girl': 0.0238037109375
		 },
		 {
		  'boy': 0.0086517333984375,
		  'eyes': 0.0077972412109375,
		  'fashion': 0.0270538330078125,
		  'facial expression': 0.00783538818359375, 
		  'music': 0.00846099853515625, 
		  'browse': 0.00992584228515625,
		  'light': 0.00835418701171875,
		  'wealthy': 0.00717926025390625,
		  'men': 0.00981903076171875,
		  'smoke': 0.006793975830078125,
		  'face': 0.0162506103515625,
		  'woman': 0.01036834716796875,
		  'studio': 0.01097869873046875,
		  'female': 0.00852203369140625,
		  'pineapple': 0.0196990966796875,
		  'portrait': 0.135498046875,
		  'model': 0.037933349609375,
		  'girl': 0.01322174072265625,
		  'black and white': 0.01206207275390625,
		  'man': 0.011138916015625
		  },
		{
		 'boy': 0.007747650146484375,
		 'eyes': 0.0124664306640625,
		 'fashion': 0.0369873046875,
		 'kids': 0.005706787109375,
		 'learning': 0.006931304931640625,
		 'sitting': 0.006256103515625,
		 'browse': 0.00951385498046875,
		 'light': 0.007724761962890625,
		 'colour': 0.006313323974609375,
		 'children': 0.00666046142578125,
		 'face': 0.0149078369140625,
		 'hair': 0.0072021484375,
		 'woman': 0.01548004150390625,
		 'studio': 0.01544952392578125,
		 'smile': 0.0057220458984375,
		 'female': 0.00919342041015625,
		 'pineapple': 0.0216217041015625,
		 'portrait': 0.112060546875,
		 'model': 0.059783935546875,
		 'girl': 0.0238037109375
		 },
		 {
		  'boy': 0.0086517333984375,
		  'eyes': 0.0077972412109375,
		  'fashion': 0.0270538330078125,
		  'facial expression': 0.00783538818359375, 
		  'music': 0.00846099853515625, 
		  'browse': 0.00992584228515625,
		  'light': 0.00835418701171875,
		  'wealthy': 0.00717926025390625,
		  'men': 0.00981903076171875,
		  'smoke': 0.006793975830078125,
		  'face': 0.0162506103515625,
		  'woman': 0.01036834716796875,
		  'studio': 0.01097869873046875,
		  'female': 0.00852203369140625,
		  'pineapple': 0.0196990966796875,
		  'portrait': 0.135498046875,
		  'model': 0.037933349609375,
		  'girl': 0.01322174072265625,
		  'black and white': 0.01206207275390625,
		  'man': 0.011138916015625
		  },
		{
		 'boy': 0.007747650146484375,
		 'eyes': 0.0124664306640625,
		 'fashion': 0.0369873046875,
		 'kids': 0.005706787109375,
		 'learning': 0.006931304931640625,
		 'sitting': 0.006256103515625,
		 'browse': 0.00951385498046875,
		 'light': 0.007724761962890625,
		 'colour': 0.006313323974609375,
		 'children': 0.00666046142578125,
		 'face': 0.0149078369140625,
		 'hair': 0.0072021484375,
		 'woman': 0.01548004150390625,
		 'studio': 0.01544952392578125,
		 'smile': 0.0057220458984375,
		 'female': 0.00919342041015625,
		 'pineapple': 0.0216217041015625,
		 'portrait': 0.112060546875,
		 'model': 0.059783935546875,
		 'girl': 0.0238037109375
		 }]

api.add_resource(MovieTags, "/api/get-tags")


if __name__ == "__main__":
    app.run()

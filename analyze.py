import operator
import models


def remove_outliers(imgs, tolerance=10):
	tags = {}
	for img in imgs:
		for key in img:
			if key in tags:
				# add probability to total
				tags[key] += img[key]
			elif key != "blur" and key != "shadow" and key != "one":
				tags[key] = img[key]

	top = dict(sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)[:tolerance])

	new_imgs = []

	for img in imgs:
		new_img = {}
		for key in img:
			if key in top:
				new_img[key] = img[key]
		new_imgs.append(new_img)

	return new_imgs


def get_tag(tag):
	movies = models.Movie.objects()
	mvs = {}
	for movie in movies:
		sum_all_tags = sum([sum(i) for i in (map(lambda x: x.values(), movie.imgs))])
		sum_tag = 0
		for frame in movie.imgs:
			if tag in frame:
				sum_tag += frame.values()[0]
		probability = (sum_tag) / sum_all_tags
		mvs[movie.name] = probability

	return sorted(mvs.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]



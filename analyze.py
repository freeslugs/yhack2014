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
     probs = []
     for movie in movies:
         sum_all_tags = sum( map(lambda x: x.values()[0], movie.imgs) )
         sum_tag = sum( map(lambda x: x.values()[0], filter(lambda y: y.keys()[0]==tag, movie.imgs)) )
         probability = (sum_tag+0.0)/sum_all_tags
         print sum_tag
         print sum_all_tags
         mvs[movie.name] = probability
         probs.append(probability)
     
     #return sorted(mvs.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]
     return probs
     


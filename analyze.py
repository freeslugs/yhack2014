import operator

def remove_outliers(imgs, tolerance=10):
	tags = {}
	for img in imgs:
		for key in img:
			if key in tags:
				# add probability to total
				tags[key] += img[key]
			else:
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
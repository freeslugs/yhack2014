import requests

access_token = "bNp6k4DquijfjRDZ1TZ3OIh9KY9KkH" 

def get_access_token():
	r = requests.post("https://api.clarifai.com/v1/token/?grant_type=client_credentials&client_id=urXuu-oV3NBj4WL8WUW37cPWlc1qDImDndJeDCc-&client_secret=LVqjz3Jhjb3xrM1IktglejjXLHZ-9e5QLJknvZAQ")
	access_token = r.json()['access_token']
	return access_token

def get_tags(url):
	global access_token
	r = requests.get('https://api.clarifai.com/v1/tag/?url='+url+'&access_token='+access_token)
	if r.status_code != 200:
		access_token = get_access_token()
		return get_tags(url)

	d = extract_tags_dict(r.json())

	return d


def get_tags_from_file(filename):
	global access_token
	files = {'encoded_image': open(filename, 'rb')}
	r = requests.post('https://api.clarifai.com/v1/tag/?access_token='+access_token, files=files)

	if r.status_code != 200:
		access_token = get_access_token()
		return get_tags(filename)

	d = extract_tags_dict(r.json())

	return d


def extract_tags_dict(obj):
	data = obj['results'][0]['result']['tag']
	tags = data['classes']
	probs = data['probs']
	return dict(zip(tags, probs))


result = get_tags_from_file('frame120.png')


for key in result:
	print key, ":", result[key]

#print get_tags('http://static.shop033.com//resources/18/160536/Image/white-cat-blue-eyes-640x360.jpg')
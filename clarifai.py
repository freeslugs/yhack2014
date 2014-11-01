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

	data = r.json()['results'][0]['result']['tag']
	tags = data['classes']
	probs = data['probs']
	d = dict(zip(tags, probs))

	for key in d:
		print key, ":", d[key]

	return d

# print get_tags('http://static.shop033.com//resources/18/160536/Image/white-cat-blue-eyes-640x360.jpg')
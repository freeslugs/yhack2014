import requests

access_token = "1INOKIFjD8v6Lv1Swf2qgdOAWmBNhC"

def get_access_token():
	r = requests.post("https://api.clarifai.com/v1/token/?grant_type=client_credentials&client_id=urXuu-oV3NBj4WL8WUW37cPWlc1qDImDndJeDCc-&client_secret=LVqjz3Jhjb3xrM1IktglejjXLHZ-9e5QLJknvZAQ")
	access_token = r.json()['access_token']
	return access_token

def get_tags(url):
	global access_token
	r = requests.get('https://api.clarifai.com/v1/tag/?url='+url+'&access_token='+access_token)
	if r.status_code != 200:
		if r.status_code == 401:
			access_token = get_access_token()
			return get_tags(url)	
		print "Error: " + r.json()['results'][0]['result']['error']
		return None
		
	d = extract_tags_dict(r.json())

	return d


def get_tags_from_file(filename):
	global access_token
	files = {'encoded_image': open(filename, 'rb')}
	r = requests.post('https://api.clarifai.com/v1/tag/?access_token=' + access_token, files=files)
	if r.status_code != 200:
		if r.status_code == 401:
			access_token = get_access_token()
			return get_tags_from_file(filename)
		print "Error: " + r.json()['results'][0]['result']['error']
		return None

	d = extract_tags_dict(r.json())

	return d

def extract_tags_dict(obj):
	data = obj['results'][0]['result']['tag']
	tags = data['classes']
	probs = data['probs']
	return dict(zip(tags, probs))



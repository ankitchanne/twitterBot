
import requests
import json

def shorturl(longUrl):
	api_key = 'AIzaSyC9CK89hnPM22XtynvVSojElqiQyillElI'
	url = 'https://www.googleapis.com/urlshortener/v1/url?key='+api_key
	payload = {'longUrl':longUrl}
	headers = {'content-type':'application/json'}
	response = requests.post(url,headers=headers,data=json.dumps(payload))
	shortURL = json.loads(response.text)
	return shortURL['id']
import requests
import json
def review(book):
	book = book.replace(' ','+')
	url = 'http://idreambooks.com/api/books/reviews.json?q='+book+'&key=8697490e7b454f806334a2b1079ec4ebd9a5b5db'
	#print url
	resp = requests.get(url)
	resp = json.loads(resp.content)
	#print resp
	review = ""
	if resp['total_results'] != 0:
		for a in resp['book']['critic_reviews']:
			review =a['source'].encode('utf-8','ignore')+' rated this '+str(a['star_rating'])+'/5 : '+a['snippet'].encode('utf-8','ignore')
			return review
			break
	else:
		review = "empty"
		return review
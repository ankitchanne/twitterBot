from guttenberg import gutten
from critic import review
from amazonfirst import amazon
from urlshort import shorturl
from TwitterAPI import TwitterAPI

def bookReply(a,api):
	name = a['text'].split('/')[2]
	title, amazonLink = amazon(name)
	gutlink = gutten(name)
	print gutlink
	msg = review(name)
	print msg
	shortLink = shorturl(amazonLink)
	answer = "Hey, I found "+title+'. Here\'s the amazon link :'+shortLink
	reply = "@"+a['user']['screen_name']+" "+answer
	resp = api.request('statuses/update',{'status':reply,'in_reply_to_status_id':a['id']})
	if gutlink != 'empty':
		fullbook = gutlink.split('//')[1]
		answer ="Thanks to guttenberg project. You can read the entire book here "+ fullbook
		reply = "@"+a['user']['screen_name']+" "+answer
		resp = api.request('statuses/update',{'status':reply,'in_reply_to_status_id':a['id']})
	if msg != 'empty':
		answer = "Here are some reviews: "+msg.decode('utf-8','ignore')
		reply = "@"+a['user']['screen_name']+" "+answer
		resp = api.request('statuses/update',{'status':reply,'in_reply_to_status_id':a['id']})
		print resp
	#print resp
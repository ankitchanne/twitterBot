from TwitterAPI import TwitterAPI
from random import randint
consumer_key = 'ICC3jFSt77w2T31jfaNSHqzRd'
consumer_secret = 'f1yQVkjuwNcZqHeESpVycFmxnl8AJasAE1gQAZ6gzbjxrd1v4W'
access_token_key = '1464509077-P0iFFOLC6DhiNWIT8g4mZfeDatMsCvywJPTTzHS'
access_token_secret = 'iTfB7685zD2OzKOtB1tjYkmP0YutZJWx8k8hrN6Fkx9hw'
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
found = 0
f = open('allMentions','r+')
mentions = api.request('statuses/mentions_timeline')
count =0
responseId = []
for a in mentions:
	responseId.append(str(a['id']))
#print responseId
#responseId.sort(reverse=True)
line = f.readline()
replies = api.request('statuses/mentions_timeline',{'since_id':line})
for a in replies:
	id = a['id']
	print id
	reply = "@"+a['user']['screen_name']+" found you bitch!"+str(randint(0,9))
	print reply
	resp = api.request('statuses/update',{'status':reply,'in_reply_to_status_id':id})
	reply = "@"+a['user']['screen_name']+" found you bitch!"+str(randint(0,9))
	resp = api.request('statuses/update',{'status':reply,'in_reply_to_status_id':id})
	#print resp.text

for i in responseId:
	if i == line:
		break
	else:
		print "writing: "+ i
		w = open('allMentions','w')
		w.write(i)
		f.close()
		break


#print line

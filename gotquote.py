import requests
import json

url = "https://got-quotes.herokuapp.com/quotes"
reply = requests.get(url)
reply = json.loads(reply.content)
print reply['quote']+' - '+reply['character'].decode('utf-8','ignore')
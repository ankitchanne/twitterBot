from bs4 import BeautifulSoup
import requests
import re

def gutten(product):
	url = 'https://www.gutenberg.org/ebooks/search/?query=t.'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	product = product.replace(" ",'+')
	url = url+product
	found = 0
	req = requests.get(url,headers=headers)
	soup = BeautifulSoup(req.content,'html.parser')
	for a in soup.find_all('a',accesskey=True):
		value = a['href']
		if re.match('/ebooks/[0-9+]',value):
			booklink = value
			found = 1
			break
	if found == 1:
		bookUrl = 'https://www.gutenberg.org/'+booklink
		req = requests.get(bookUrl,headers=headers)
		soup = BeautifulSoup(req.content,'html.parser')
		for a in soup.find_all('a',title=True):
			if a['title'] == 'Download':
				bookHTMLLink =  a['href']
				break
	else:
		bookHTMLLink = "empty"

	return bookHTMLLink
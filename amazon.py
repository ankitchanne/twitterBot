from bs4 import BeautifulSoup
#from bs4 import UnicdeDammit
import requests
import re





def amazon(product):
	url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	product = product.replace(" ",'+')
	url = url+product
	req = requests.get(url,headers=headers)
	soup = BeautifulSoup(req.content,'html.parser')
	title = soup.find_all('a',title=True)[0]['title']
	link = soup.find_all('a',title=True)[0]['href']
	money = soup.find_all('span',class_='s-price')[0]
	money = money.text
	result = title + " for Rs." + money.strip()
	return result, link

def flipkart(product):
	info = []
	name = product
	product = product.replace(" ",'%20')
	result = "Nothingfound!"
	finalLink = 'none'
	url = 'https://www.flipkart.com/search?q='+product+'&otracker=start&as-show=off&as=off'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	req = requests.get(url,headers=headers)
	#print req.content.decode('utf-8','ignore')
	soup = BeautifulSoup(req.content.decode('utf-8','ignore'),'html.parser')
	for a in soup.find_all('a',title=True):
		print 'in here.. '
		c =  a.text.lower()
		if name in c:
			title = a.text
			href = a['href']
			#print title
		
			sibiling = a.parent
			for k in sibiling.find_all('div'):
				#print "---------------"
				if k.findChildren() == []:
					info.append(k.text.encode('ascii',errors='ignore'))
			#print info
			result = title+" for Rs. "+info[2]
			break
		else:
			result = "Nothing found on flipkart!"
	for b in soup.find_all('a',href=True):
		if 'pid' in b['href']:
			finalLink = "www.flipkart.com"+b['href']
			break
	
	return result, finalLink

def gutten(product):
	url = 'https://www.gutenberg.org/ebooks/search/?query='
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
		bookHTMLLink = "Nothing found on guttenberg.."

	return bookHTMLLink



product = 'harry potter and philosophers stone'

'''amazonResult = amazon(product)
flipkartResult = flipkart(product)
guttenLink = gutten(product)
print amazonResult
print flipkartResult
print guttenLink		
'''
flipcost,fliplink = flipkart(product)
print flipcost, fliplink
cost,link = amazon(product)
print cost,link
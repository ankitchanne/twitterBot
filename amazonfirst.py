from bs4 import BeautifulSoup
import requests

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
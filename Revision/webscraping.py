from bs4 import BeautifulSoup
import requests


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')



article = soup.find_all('div',class_='container')
print(article)


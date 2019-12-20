import requests 
from bs4 import BeautifulSoup as soup  
import base64 

""" url = "https://bastien-ltn.fr/cmd/"
data = requests.get(url)

data2 = soup(data.text,"html.parser")

cmd = data2.find('div', {"class": "entry-content"}).find("p").string

cmd = str(base64.b64decode(cmd), 'utf-8') """


url = "https://twitter.com/S1mpleCC"
data = requests.get(url)
data = soup(data.text,"html.parser")
cmd = data.find('div', {'class':'tweet'}).find('p', {'class': 'tweet-text'}).string
#timeTweet = data.find('div', {'class':'tweet'}).find('span', {'class':'_timestamp'}).attrs.get.('data-time-ms')

print(timeTweet)

import requests 
from bs4 import BeautifulSoup as soup   

url = "https://www.leboncoin.fr/"
data = requests.get(url)

data2 = soup(data.text,"html.parser")
print(data2)
print(type(data2))
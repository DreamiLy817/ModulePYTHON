#coding:utf-8

import socket as sock

mon_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

mon_socket.bind(("", 5678))
mon_socket.listen(5)

conf, info = mon_socket.accept()

print("Connexion établie de : {}".format(info))

cmd = ""
while cmd != "quit()" :
    cmd = input("Cmd :> ")
    conf.send(cmd.encode('UTF-8'))
    data = conf.recv(1024)
    print(data.decode('UTF-8'))

conf.close()
mon_socket.close()

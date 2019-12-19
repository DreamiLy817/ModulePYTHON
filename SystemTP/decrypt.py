from cryptography.fernet import Fernet as fernet
import os

with open("/root/script/key.txt", "r") as f:
    key = f.read()

algo = fernet(key.encode())

for dirpath, dirnames, files in os.walk('/root/script/Private', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        with open(dirpath+ "/" + file_name, "rb") as f:
            data = f.read()
        dataDecrypt = algo.decrypt(data)
        dataDecrypt = dataDecrypt.decode('UTF-8')

        with open(dirpath+ "/" + file_name, "w") as n:
            n.truncate(0)
            n.write(str(dataDecrypt))
            print('Fichier dechiffre:' + dirpath+ "/" + file_name)


print('Dechiffrement des fichiers termines')
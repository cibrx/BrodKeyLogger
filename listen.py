import socket
from cryptography.fernet import Fernet
import datetime

port = 64647  # Gönderilen broadcast mesajının portu

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', port))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        time = datetime.datetime.now()
        logs = open("logs/log_"+str(time.day)+"__"+str(time.hour)+":"+str(time.minute),"a")
        key = "eVb-cKIXtOH4W1iD-3X62m8XgIKX8d34dyJsuQ3EU8I="
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(data)
        print(decrypted_data.decode())
        logs.write(str(decrypted_data))


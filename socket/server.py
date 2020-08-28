import socket
import sys

def create_socket():
    try:
        global host
        global port
        global a
        host = ""
        port = 3333
        a = socket.socket()
    except socket.error as msg:  
        print("socket error",msg)
     
#**************************************************** binding and listening socket **********************************

def bind_socket():
 try:
    global host
    global port
    global a
    print("port binding"+str(port))
    a.bind((host,port))
    a.listen(5)
 except socket.error as msg:
     print("socket binding err"+str(msg)+'Retrying...')
     bind_socket()
     

#**************************************************** connection with client ******************************************************************
def socket_accept():
    global host
    global port
    global a
    con,add = a.accept()
    print(f"connection is done","Ip:",str(add[0]),"port",int(add[1]))
    send_command(con)
    a.close()

#********************************************************* send command  ******************************************************************    
def send_command(con):
    while True:
        cmd = input()
        if(cmd == 'quit'):
            cmd.close()
            a.close()
            sys.exit()
        if(len(str.encode(cmd)) > 0):
            con.send(str.encode(cmd))
            client_response = str(con.recv(1024),"utf-8")
            print(client_response,end="")
            
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

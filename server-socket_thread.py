# echo-server.py
from threading import Thread
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT =  9999  # Port to listen on (non-privileged ports are > 1023)

class mt(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        print(f'connection established with{addr[0]}')

    def run(self):
        with conn:
            print(f"Connected by {addr}")
            data=conn.recv(1024)
            while data:
                print(f'{addr[0]} : ',data.decode())
                if not data:
                    break
                data = conn.recv(1024)

        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        mt(conn,addr).start()
    
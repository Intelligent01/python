from subprocess import Popen,PIPE,STDOUT
from threading import Thread 
import socket
import mimetypes as mi


resphdr="""HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Type: {type}
Accept-Ranges: bytes
Content-Length: {clen}
Vary: Accept-Encoding
Server: Apache/2.4.41 (Ubuntu)

{body}"""

class mlt(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        print(f'connection established with {addr[0]} :')
    
    def run(self):
        with self.conn:
            data=self.conn.recv(1024)
            while data:
                if not data:
                    break

                hr=data.decode().split('\n')[0].split(' ')[1]
                if hr=='/':
                    with open('index.html') as ind:
                        content=ind.read()
                    aa=resphdr.format(type=mi.guess_type('index.html')[0],body=content.replace('\n','<br>').encode(),clen=len(content))
                    # print(aa.replace("\\n","<br>"))
                    self.conn.sendall(aa.encode())



                data=conn.recv(1024)





s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9999))
s.listen()

while True:
    conn,addr=s.accept()
    mlt(conn,addr).start()


        
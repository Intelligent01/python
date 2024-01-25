import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
a=input('--->')
while a != 'bye':
    s.send(a.encode())
    a=input('--->')
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))
    while True:
        data = s_sock.recv(2048)
        print(data)
        if not data:
            break
        s_sock.sendall(str.encode(ok_message))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")



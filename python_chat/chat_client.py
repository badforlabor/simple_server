from socket import *

HOST = 'localhost'
PORT = 55556
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
          data = input('>')
          if not data:
                    break
          tcpCliSock.send(data.encode("utf-8"))
          data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
          if not data:
                    break
          print(data)
tcpCliSock.close();
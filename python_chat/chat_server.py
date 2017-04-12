from socket import *
from time import ctime

HOST = 'localhost'
PORT = 55556
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(8)

print ('start server... \n ip  ',HOST,' \n port', PORT   )

while True:
          print("Waiting for connection...")
          tcpCliSock, addr = tcpSerSock.accept()
          print("...connected from:",addr)
          while True:
                    data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
                    if not data:
                              break
                    tcpCliSock.send(('[%s] %s' % (bytes(ctime(),'utf-8'),data)).encode("utf-8"))
                    tcpCliSock.send("hello".encode("utf-8"))
          tcpCliSock.close()
tcpSerSock.close()
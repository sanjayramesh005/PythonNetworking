#This server just sends back the data it receives to the same cient which sent it.
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '' # symbolic meaning of all available interfaces.
port = 1234

serversocket.bind((host,port))
serversocket.listen(5)
print "Server started. Waiting for client...."

clientsocket, addr = serversocket.accept()
print "Connected to" , addr

while True:
    data = clientsocket.recv(1024)
    if not data:
        break
    else:
        clientsocket.sendall(data)

clientsocket.close()

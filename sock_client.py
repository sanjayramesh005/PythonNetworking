#This client doenot send the server any data. It only receives data.
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '202.3.77.237'
port = 1234

clientsocket.connect((host,port))

data = clientsocket.recv(1024)

clientsocket.close()

print "The time obtained from the server is ", data#.decode('ascii')

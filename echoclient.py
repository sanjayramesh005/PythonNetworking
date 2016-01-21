import socket

host = socket.gethostname()
port = 1234

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host,port))
clientsocket.sendall("Hello World")
data = clientsocket.recv(1024)
clientsocket.close()
print "Received:", data

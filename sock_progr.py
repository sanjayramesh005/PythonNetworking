#This server doesnot receive any data from the client. It just creates a socket.
import socket
import time

#create a socket with the given socket family(AF_INET), and socket type(SOCK_STREAM) and protocol number- usually taken to be default(0).
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '202.3.77.237'#Get the name of the local machine
port = 1234

serversocket.bind((host,port))#bind to the port

serversocket.listen(5) #queue up to 5 requests
print "Server started. Waiting for client...."

while True:
    clientsocket, addr = serversocket.accept()#establish connection
    print "Got a connection from", addr
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode("ascii"))
    clientsocket.close()

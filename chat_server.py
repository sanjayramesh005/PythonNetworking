import socket
import sys
import select

host = ''
port = 1234
buffer_size = 4096
sockets = []
def chat_server():
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((host, port))
        serversocket.listen(10)

        sockets.append(serversocket)

        print "Chat server started on port " + str(port)
        while True:
                readable, writable, err = select.select(sockets, [], [], 0)

                for sock in readable:
                        if sock == serversocket:
                                clientsocket, addr = serversocket.accept()
                                sockets.append(clientsocket)
                                print "Client", addr , "connected."

                                broadcast(serversocket,clientsocket, "[%s:%s] entered the chat room\n")

                        else:
                                try:
                                        data = sock.recv(buffer_size)
                                        if data:
                                                braoadcast(serversocket, sock, "\r"+"["+str(sock.getpeername())+']'+data)
                                        else:
                                                if sock in sockets:
                                                        sockets.remove(sock)
                                                        broadcast(serversocket,sock,"Client [%s:%s] is offline.\n" % addr )
                                except:
                                        broadcast(serversocket, sock, "Client [%s:%s] is offline.\n" % addr)
                                        continue
        serversocket.close()

        
def broadcast(serversocket, sock, message):
        for socket in sockets:
                if socket!=serversocket and socket!=sock:
                        try:
                                socket.send(message)
                        except:
                                socket.close()
                                if socket in sockets:
                                        sockets.remove(socket)
if __name__ == "__main__":
        sys.exit(chat_server())

"""serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((host,port))
print "Server Started."
serversocket.listen(10)
sockets = [serversocket]
err = []

def broadcast(data,sock):
        for i in sockets:
                if (i!=sock):
                        i.sendall(data)


while True:
	readable, writable, err = select.select(sockets, sockets, err, 0)
	for sock in sockets:
		if (serversocket in readable):
			clientsocket, addr = serversocket.accept()
			broadcast("Connected: "+str(addr),None)
			sockets.append(clientsocket)
			clientsocket.send("Thanks for connecting.")
			a.pop(serversocket)
		if readable:
			for sock in readable:
				data = sock.recv(buffer_size)
				broadcast(data,sock)"""

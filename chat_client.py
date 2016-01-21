import sys
import select
import socket

def chat_client():
    if (len(sys.argv) < 3):
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    #try:
    s.connect((host,port))
    #except:
        #print "Unable to connect."
        #sys.exit()

    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()

    while True:
        socket_list = [sys.stdin, s]

        readable, writable, err = select.select(socket_list, [], [])
        for sock in readable:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server.'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()

            else:
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())

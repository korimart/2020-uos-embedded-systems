import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind(("192.168.137.1", 8080))
# become a server socket
serversocket.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print(address)
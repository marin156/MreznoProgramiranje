#tcp_client.py

import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 9999

client_socket.connect((host,port))
#print client_socket.recv(1024)
print host
client_socket.close()
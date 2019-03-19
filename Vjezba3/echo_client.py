#echo_server.py

import socket
import datetime

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host, port))

text_to_send = raw_input(">>>>> ")

print datetime.datetime.now()
client_socket.sendall(text_to_send)

data = client_socket.recv(1024)

print data
client_socket.close()

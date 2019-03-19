#echo_server.py

import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print datetime.datetime.now()
print "Cekam klijenta..."
#conn, addr = echo_server.accept()

print "Spojen: "

print "Machine_info_print: => ", print_machine_info()

while True:
	conn, addr = echo_server.accept()
	data = conn.recv(1024)
	if not data: break
	
	if data == 'aspira':
		conn.sendall('Ne moze.')

	else: 
		conn.sendall(data)

		

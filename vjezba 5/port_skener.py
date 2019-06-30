import socket
import datetime
from local_machine_info import print_machine_info

datum = datetime.datetime.now()
print(datum)
print_machine_info()

host = raw_input("Unesite adresu hosta koju zelite testirati: ")
host_ip = socket.gethostbyname(host)
print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje")
start = raw_input("Pocetni port: ")
end = raw_input("Zavrsni port: ")

for port in range(int(start), int(end)+1):
	print("Skeniram port %d") % (port)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	result = s.connect_ex((host,port))
	if result == 0:
		print "Port is open"
	else:
		print "Port is not open"
	s.close()

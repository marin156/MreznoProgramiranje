import socket
import datetime
from local_machine_info import print_machine_info
from Queue import Queue
import threading
import os


def check_ping(hostname):
    response = os.system("ping -n 1 " + hostname)
	
    return response

def scanPort(port):
	print("Skeniram port %d") % port

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	result = s.connect_ex((host,port))
	if result == 0:
		print "Port is open"
	else:
		print "Port is not open"
	s.close()
	

def worker():
    while True:
        port = q.get()
        scanPort(port)
        q.task_done()


		
datum = datetime.datetime.now()
print(datum)
print_machine_info()


host = raw_input("Unesite adresu hosta koju zelite testirati: ")
print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje")
start = raw_input("Pocetni port: ")
end = raw_input("Zavrsni port: ")
print("Provjeravam je li host dostupan")

q = Queue()

if check_ping(host) == 0:
	for i in range(3):
		t = threading.Thread(target=worker)
		t.daemon = True
		t.start()

	for port in range(int(start), int(end)+1):
		q.put(port)
else:
	print("Host nije dostupan")
	

q.join()       # block until all tasks are done



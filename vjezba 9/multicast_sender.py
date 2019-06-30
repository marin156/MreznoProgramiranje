import socket
import struct
import sys

import datetime

from local_machine_info import print_machine_info
if __name__ == '__main__':

	datum = datetime.datetime.now()
	print(datum)
	print_machine_info()

message = 'Test - mdruzijanic' 
multicast_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(0.2)

try:

    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(
                data, server))

finally:
    print('closing socket')
    sock.close() 
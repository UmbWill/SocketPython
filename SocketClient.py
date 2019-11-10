import socket
import time
HOST = '127.0.0.1'
PORT = 65432

while True:
	time.sleep(0.5)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))	
	#s.sendall(b'Hello, world')
	s.sendall(b'[xFF,xFF,xFF]')
	s.shutdown(socket.SHUT_WR)
	data = b''
	while True:
		buf = s.recv(1024)
		if not buf:
			break
		data += buf
	s.close()
print('Received', repr(data))
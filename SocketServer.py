import socket

HOST = ''
PORT = 65435 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
while True:
	conn, addr = s.accept()
	print('Connected by', addr)
	data = ""
	while True:
		data = conn.recv(1024)
		print(data)
		if data : break
	if data == "exit":break
	conn.sendall(b'ok')
	conn.shutdown(socket.SHUT_WR)
conn.close()
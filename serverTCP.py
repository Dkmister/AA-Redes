import sys
import socket
import time
import logging

logging.basicConfig(filename='TCP_server.log',level = logging.DEBUG,filemode='w')

TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2])

BUFFER_SIZE = 1024
n_pac=0
delta=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Endereco de conexao::', addr)
while True:
	t1 = time.time()
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	conn.send(data) # echo
	t2 = time.time()
	delta += (t2-t1)
	n_pac+=1
	if delta > 1:
		band = (n_pac * 8 * 1000)/delta
		logging.info('%f bps',band)
		logging.info('endereco: %s',addr)
		n_pac = 0
		delta = 0
conn.close()

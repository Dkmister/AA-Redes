import socket
import time
import logging

logging.basicConfig(level=logging.INFO)

TCP_IP = '192.168.0.10'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Endereco de conexao::', addr)
while True:
	t1 = time.time()
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("Dados recebidos:", len(data))
	conn.send(data) # echo
	t2 = time.time()
conn.close()

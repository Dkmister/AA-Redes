import sys
import socket
import time
import logging
time_actual = time.time()
logging.basicConfig(filename='{}'.format(time_actual),level = logging.DEBUG,filemode='w')

if len(sys.argv) != 3:
	print('Usage: python3 serverTCP.py localIP port')
	sys.exit(1)

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
	if not data: break # echo
	t2 = time.time()
	delta += (t2-t1)
	n_pac+=1
	if delta > 1:
		band = (n_pac * 8 * 1000)/delta
		if band > 10 ** 9:
			logging.info('%f Gbps', 10 * band / 10 ** 9)
		elif band < 10 ** 9 and band > 10 ** 6:
			logging.info('%f Mbps', 8 * band / 10 ** 6)
		elif band < 10 ** 6 and band > 10 ** 3:
			logging.info('%f Kbps', 10 * band / 1000)
		else:
			logging.info('%f bps',10 * band)
		logging.info('endereco: %s',addr)
		n_pac = 0
		delta = 0
conn.close()

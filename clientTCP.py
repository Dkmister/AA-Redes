import socket 
import sys 

if len(sys.argv)!=3:
	print('Usage: python3 clientTCP.py destinationIP port')
	sys.exit(1)

TCP_IP =  sys.argv[1]
TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024
MESSAGE = bytes(1000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)

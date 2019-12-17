import sys
import matplotlib.pyplot as plt

if len(sys.argv)!=2:
	print('Usage: python3 log_extract.py filename')
	sys.exit(1)
	
filename = sys.argv[1]

lst_band = []

with open(filename,'r') as data:
	for line in data.readlines():
		lst_band.append(float(line[10::].rstrip()))

plt.plot(lst_band)
plt.ylabel('Mbps')
plt.show()

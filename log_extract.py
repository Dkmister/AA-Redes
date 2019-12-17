import sys
import matplotlib.pyplot as plt

if len(sys.argv)!=4:
	print('Usage: python3 log_extract.py filename filename filename')
	sys.exit(1)
	
filename1 = sys.argv[1]
filename2 = sys.argv[2]
filename3 = sys.argv[3]

lst_band1 = []
lst_band2 = []
lst_band3 = []

with open(filename1,'r') as data:
	for line in data.readlines():
		lst_band1.append(float(line[10::].rstrip()))

with open(filename2,'r') as data:
	for line in data.readlines():
		lst_band2.append(float(line[10::].rstrip()))

with open(filename3,'r') as data:
	for line in data.readlines():
		lst_band3.append(float(line[10::].rstrip()))




while(len(lst_band1) != len(lst_band2)):
	lst_band2.insert(0,0.0)

while(len(lst_band1) != len(lst_band3)):
	lst_band3.insert(0,0.0)



plt.plot(lst_band1)
plt.plot(lst_band2)
plt.plot(lst_band3)
plt.ylabel('bps')
plt.xlabel('tempo')
plt.title('Banda ao longo do tempo')
plt.show()


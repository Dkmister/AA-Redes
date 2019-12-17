import sys

if len(sys.argv)!=2:
	print('Usage: python3 log_extract.py filename')
	sys.exit(1)
	
filename = sys.argv[1]

lst_band = []

with open(filename,'r') as data:
	for line in data.readlines():
		lst_band.append(line[10::].rstrip())

print(lst_band)

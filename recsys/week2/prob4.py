import sys
import operator
from collections import defaultdict

file1 = open('recsys_rating_matrix.csv', 'r').read()
header = file1.replace('\r','\n').split('\n')[0].split(',')
lines = file1.replace('\r','\n').split('\n')[1:-2]
a_dict = defaultdict(int)
b_dict = defaultdict(int)
for line in lines:
	words = line.split(',')
	for i in range(1,21):
		if words[i] != '':
			b_dict[i] += 1
			if words[1] != '':
				a_dict[i] += 1

for i in range(1,21):
	print a_dict[i], b_dict[i]
	a_dict[i] = a_dict[i]*1.0/b_dict[i]
print a_dict
sorted_x = sorted(a_dict, key=a_dict.get, reverse=True)
print sorted_x
for i in sorted_x[1:6]:
	print header[i]
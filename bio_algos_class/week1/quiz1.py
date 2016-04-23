def occurrences(string, sub):
  count = start = 0
  while True:
      start = string.find(sub, start) + 1
      if start > 0:
          count+=1
      else:
          return count

with open('dataset_2_6.txt', 'r') as f:
	txt = f.readline().strip('\n')
	pattern = f.readline().strip('\n')

	print occurrences(txt, pattern)
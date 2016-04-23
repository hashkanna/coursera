# Uses python3
import sys

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max_1 = -sys.maxsize - 1
max_2 = -sys.maxsize - 2
for i in range(n):
    if a[i] > max_1:
        max_1 = a[i]
        max_ind = i

for j in range(n):
    max_2 = a[j] if a[j] > max_2 and j != max_ind else max_2

result = max_1 * max_2

print(result)

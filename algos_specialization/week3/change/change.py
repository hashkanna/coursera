# Uses python3
import sys

def get_change(n):
    #write your code here
    count = 0
    for i in [10,5,1]:
        count += (n//i)
        n %= i
    return count

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))

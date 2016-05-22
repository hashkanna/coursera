# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n+1):
        a, b = b, (a + b) % 10
    return b

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

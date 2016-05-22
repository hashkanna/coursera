# Uses python3
import sys

def gcd(a, b):
    #print(a, b)
    if b == 0: return a
    if a == 0: return b
    return gcd(b, a%b) if a > b else gcd(a, b%a)

def lcm(a, b):
    #write your code here
    return (a*b)//gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

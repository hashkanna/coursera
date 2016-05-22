# Uses python3
def calc_fib_slow(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    a = 0
    b = 1
    if (n <= 1):
        return n

    for i in range(2,n+1):
        a, b = b, a+b

    return b

n = int(input())
print(calc_fib(n))

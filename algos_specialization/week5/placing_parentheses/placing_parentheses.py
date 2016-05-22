# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i,j,m,M,operators,digits):
    #write your code here
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        #print('kanna', i, j, k)
        a = evalt(M[(i,k)], M[(k+1,j)], operators[k-1])
        b = evalt(M[(i,k)], m[(k+1,j)], operators[k-1])
        c = evalt(m[(i,k)], M[(k+1,j)], operators[k-1])
        d = evalt(m[(i,k)], m[(k+1,j)], operators[k-1])
        #print('haha', a, b, c, d)
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return (min_val, max_val)

def get_maximum_value(dataset):
    operators = dataset[1::2]
    digits = list(map(int, dataset[::2]))
    n = len(digits)
    m = {}
    M = {}
    for i in range(1,n+1):
        m[(i,i)] = digits[i-1]
        M[(i,i)] = digits[i-1]
    #print(m, M)
    for s in range(1,n):
        for i in range(1,n-s+1):
            j = i + s
            #print(i,j)
            m[(i,j)], M[(i,j)] = MinAndMax(i,j,m,M,operators,digits)
    #print(m, M)
    return M[(1,n)]


if __name__ == "__main__":
    print(get_maximum_value(input()))

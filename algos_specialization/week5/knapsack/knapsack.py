# Uses python3
import sys

def optimal_weight_list(W, w):
    # write your code here
    j = len(w)
    value = [[0] * (j+1)] * (W+1)
    #for x in range(j+1): value[(0,x)] = 0
    #for x in range(W+1): value[(x,0)] = 0

    for i in range(1, j+1):
        for ww in range(1, W+1):
            value[ww][i] = value[ww][(i-1)]
            #print(i)
            if w[i-1] <= ww:
                val = value[ww-w[i-1]][i-1] + w[i-1]
                if value[ww][i] < val:
                    value[ww][i] = val
    print(value)
    return value[W][n]

def optimal_weight_dict(W, w):
    # write your code here
    j = len(w)
    value = {}
    for x in range(j+1): value[(0,x)] = 0
    for x in range(W+1): value[(x,0)] = 0

    for i in range(1, j+1):
        for ww in range(1, W+1):
            value[(ww,i)] = value[(ww,(i-1))]
            #print(i)
            if w[i-1] <= ww:
                val = value[(ww-w[i-1],(i-1))] + w[i-1]
                if value[(ww,i)] < val:
                    value[(ww,i)] = val
    print(value)
    return value[(W,n)]

    """
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
    """

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

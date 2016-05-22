# Uses python3
import collections

def edit_distance(s, t):
    #write your code here
    d = {}
    for i in range(len(s) + 1):
        d[i,0] = i
    #print(d)
    for j in range(len(t) + 1):
        d[0,j] = j
    #print(d)
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            insertion = d[i,j-1] + 1
            deletion = d[i-1,j] + 1
            mismatch = d[i-1,j-1] + 1
            match = d[i-1,j-1]
            if s[i-1] == t[j-1]:
                d[i,j] = min(insertion, deletion, match)
            else:
                d[i,j] = min(insertion, deletion, mismatch)
    return d[len(s), len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

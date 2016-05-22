# Uses python3
import sys
import operator

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    max_values = [j/i for i,j in zip(weights, values)]
    while capacity > 0 and len(max_values) > 0:
        max_index, max_value = max(enumerate(max_values), key=operator.itemgetter(1))
        if weights[max_index] > capacity:
            value += max_values[max_index] * capacity
            capacity = 0
        else:
            value += values[max_index]
            capacity -= weights[max_index]
            del(weights[max_index])
            del(values[max_index])
            del(max_values[max_index])

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

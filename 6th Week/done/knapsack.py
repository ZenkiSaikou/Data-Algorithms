import numpy

def maxGold(W, n, items):
    value = numpy.zeros((W + 1, n + 1))
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            value[i][j] = value[i][j - 1]
            if items[j - 1] <= i:
                temp = value[i - items[j - 1]][j - 1] + items[j - 1]
                if temp > value[i][j]:
                    value[i][j] = temp
    return (int(value[W][n]), value)


def printItems(value, items, i, j, arr):
    if i == 0 and j == 0:
        arr.reverse()
        return arr
    if value[i][j] == value[i][j - 1]:
        arr.append(0)
        return printItems(value, items, i, j - 1, arr)
    else:
        arr.append(1)
        return printItems(value, items, i - items[j - 1], j - 1, arr)

if __name__ == '__main__':
    W, n = [int(i) for i in input().split()]
    item_weights = [int(i) for i in input().split()]
    max_weight, Matrix = maxGold(W, n, item_weights)
    bool_vector = printItems(Matrix, item_weights, W, n, [])
    optimal = [str(j) for i, j in enumerate(item_weights) if bool_vector[i]]
    print(f"Weights in knapsack of capacity {W}: {' '.join(optimal)}")

# Uses python3
import sys
from collections import namedtuple

n = int(input())

def segments(n):
    lst = []
    for _ in range(n):
     a, b = [int(i) for i in input().split()]
     lst.append((a, b))
    lst.sort(key=lambda y: y[1])

    index = 0
    coordinates = []

    while index < n:
        current = lst[index]
        while index < n - 1 and current[1] >= lst[index + 1][0]:
            index += 1
        coordinates.append(current[1])
        index += 1
    print(len(coordinates))
    print(' '.join([str(i) for i in coordinates]))

segments(n)
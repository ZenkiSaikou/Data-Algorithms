#Uses python3

import sys
n = int(input())

def max_dot_product(n):
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    product = sum(a[i]*b[i] for i in range(n))
    print(product)

max_dot_product(n)
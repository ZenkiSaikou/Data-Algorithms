# Uses python3
import sys

n = int(input())

if n <= 1:
    print(n)
    quit()

remainder = (n+2)%60
if remainder == 1:
    print(0)
    quit()
elif remainder == 0:
    print(9)
    quit()

def fibonacci(n):
    past, present = 0, 1
    for _ in range(2,remainder+1):
        future = past + present
        future = future % 10
        present, past = future, present
    if future != 0:
        print(future - 1)
    else:
        print(9)

fibonacci(remainder)

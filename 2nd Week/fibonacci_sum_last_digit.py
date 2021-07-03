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


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))

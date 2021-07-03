# Uses python3
n = int(input())
if n <= 1:
    print(n)
    quit()

def fibonacci(n):
    present, past = 0, 1
    for _ in range(n-1):
        future = present + past
        past, present = future, past
        print(future)

fibonacci(n)
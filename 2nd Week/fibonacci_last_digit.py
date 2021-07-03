# Uses python3
n = int(input())
if n <= 1:
    print(n)

def fibonacci(n):
    past, present = 0, 1
    for _ in range (n-1):
        future = past + present
        future = future % 10
        present, past = future, present
    print (future)

fibonacci(n)
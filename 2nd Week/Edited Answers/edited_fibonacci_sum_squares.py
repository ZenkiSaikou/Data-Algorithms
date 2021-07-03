# Uses python3

n = int(input())
remainder_n = n % 60
remainder_nadd = (n + 1) % 60

def fibonacci(n):
    past, present = 0, 1
    for _ in range(2, n + 1):
         future = past + present
         future = future % 10
         present, past = future, present
    return future

if remainder_n <= 1:
    past = remainder_n
else:
    past = fibonacci(remainder_n)

if remainder_nadd <= 1:
    present = remainder_nadd
else:
    present = fibonacci(remainder_nadd)

print((past * present) % 10)
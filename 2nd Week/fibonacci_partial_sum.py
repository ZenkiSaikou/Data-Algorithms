# Uses python3
import sys
Fvalue, Svalue = [int(i) for i in input().split()]

if Svalue <= 1:
    print(Svalue)
    quit()

remainder_Svalue = (Svalue + 2) % 60
remainder_Fvalue = (Fvalue + 1) % 60

def fibonacci(Svalue):
    past, present = 0, 1
    for i in range (2, Svalue+1):
        future = past + present
        future = future % 10
        present, past = future, present
    return (future - 1)

if remainder_Svalue <= 1:
    past = remainder_Svalue - 1
else:
    past = fibonacci(remainder_Svalue)

if remainder_Fvalue <= 1:
    present = remainder_Fvalue - 1
else:
    present = fibonacci(remainder_Fvalue)

if past >= present:
    print(past - present)
else:
    print(10 + past - present)

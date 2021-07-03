# Uses python3
import sys
m = int(input())
def change(m):
    count = 0
    for i in [10, 5, 1]:
        if m >= i:
            quotient = m // i
            count += quotient
            m = m % i
            if m == 0:
                print(count)
                quit()



change(m)
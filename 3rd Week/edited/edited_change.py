# Uses python3
import sys
minimum = int(input())
def change (minimum):
    count = 0
    for i in [10, 5, 1]:
        if minimum >= i:
            quotient = minimum // i
            count += quotient
            minimum = minimum % i
            if minimum == 0:
                print(count)
                quit()



change(minimum)
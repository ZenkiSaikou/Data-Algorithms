# Uses python3
import sys

n = int(input())

def summands(n):
    if n == 1:
      print(1)
      print(1)
      quit()
    Win = n
    prizes = []
    for i in range(1, n):
     if Win > 2 * i:
        prizes.append(i)
        Win -= i
     else:
        prizes.append(Win)
        break
    print(len(prizes))
    print(' '.join([str(i) for i in prizes]))

summands(n)
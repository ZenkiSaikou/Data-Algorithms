import math

cash = int(input())
denominations = [1, 3, 4]
minCoins = [0] + [math.inf]*cash

for i in range(1, cash+1):
    for j in denominations:
        if i>=j:
            coins = minCoins[i-j]+1
            if coins < minCoins[i]:
                minCoins[i] = coins

print(minCoins[cash])
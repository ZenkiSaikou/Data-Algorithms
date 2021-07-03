# Uses python3
import sys
Number, Weight = [int(i) for i in input().split()]
Backpack = []

if Weight == 0:
    print(0)
    quit()


for _ in range(Number):
    value, capacity = [int(i) for i in input().split()]
    if value == 0:
        continue
    # Adds the item into the Backpack
    Backpack.append((value, capacity))

Backpack.sort(key=lambda o: o[0]/o[1], reverse=True)

total_value = 0

for value, capacity in Backpack:
    if Weight == 0:
        print(total_value)
        quit()
    Amount = min(capacity, Weight)
    total_value += Amount * value / capacity
    Weight -= Amount


print(round(total_value, 4))

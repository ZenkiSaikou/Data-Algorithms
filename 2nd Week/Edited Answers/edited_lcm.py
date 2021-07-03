# Uses python3

a, b = [int(i) for i in input().split()]

def lcm(a, b):
    if b == 0:
        return a
    c = a % b
    return lcm(b, c)

if a > b:
    ans = lcm(a, b)
else:
    ans = lcm(b, a)

print(a * b // ans)
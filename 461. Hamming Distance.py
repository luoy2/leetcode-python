x = 1
y = 4

x = x ^ y
y = 0
while x:
    y += 1
    x = x & (x - 1)
    print(x)
print(y)
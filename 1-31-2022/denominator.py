x = int(input())
y = 1

while y <= x // 2:
    if x % y == 0:
        print(y)
    y += 1
print(x)
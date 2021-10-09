a, b = map(int, input().split(" "))
if b >= 45:
    print(a, b-45)
else:
    b = b + 15
    a = a - 1
    if a == -1:
        a = 23
    print(a, b)

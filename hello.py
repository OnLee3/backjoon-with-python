import sys
X = int(input())

cnt = 1
while X > cnt:
    X -= cnt
    cnt += 1

if cnt % 2 == 0:
    a = (1 + (X-1))
    b = (cnt - (X-1))
else:
    a = (cnt - (X-1))
    b = (1 + (X-1))
print(str(a) + "/" + str(b))

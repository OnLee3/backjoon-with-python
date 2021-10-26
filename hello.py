import sys

xList = []
yList = []

for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    xList.append(a)
    yList.append(b)

for i in xList:
    if xList.count(i) == 1:
        x = i
        break

for i in yList:
    if yList.count(i) == 1:
        y = i
        break

print(x, y)

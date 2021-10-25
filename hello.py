import sys
x, y, w, h = map(int, sys.stdin.readline().split())
x = min(x, (w-x))
y = min(y, (h-y))
print(min(x, y))

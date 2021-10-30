import sys

T = int(sys.stdin.readline())


def solve(x1, y1, r1, x2, y2, r2):
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if r == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 == r or r2 == r + r1 or r1 == r + r2:
        print(1)
    elif max(r1, r2, r) > r1+r2+r-max(r1, r2, r):
        print(0)
    else:
        print(2)


for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    solve(x1, y1, r1, x2, y2, r2)

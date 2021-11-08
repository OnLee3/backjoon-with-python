import sys

N = int(sys.stdin.readline())


def solve(a):
    if a > 17:
        R = a - (len(str(a))*9)
    else:
        R = 0
    for i in range(R, a):
        tmp = i
        for j in range(0, len(str(i))):
            tmp += int(str(i)[j])
        if tmp == a:
            return i
    else:
        return 0


print(solve(N))

import sys


def solve(n):
    for i in range(n//2, 1, -1):
        if L[i] == True:
            for j in range(n//2, n):
                if L[j] == True and i + j == n:
                    print(i, j)
                    break
            else:
                continue
            break


R = int(10000 ** 0.5)
L = [False, False, True] + [True, False] * 5000


for i in range(2, R+1):
    if L[i] == True:
        for j in range(i+i, 10003, i):
            L[j] = False

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    solve(n)

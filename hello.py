import sys


def solve(N):
    R = int((N*2) ** 0.5)
    M = ((N*2)+1)
    L = [True] * M
    for i in range(2, R+1):
        if L[i] == True:
            for j in range(i+i, M, i):
                L[j] = False
    print(L[N+1:M].count(True))


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    solve(N)

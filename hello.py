import sys
M, N = map(int, sys.stdin.readline().split())
R = int(N ** 0.5)
N += 1
L = [True] * (N)


def solve(N, M):
    for i in range(2, R+1):
        if L[i] == True:
            for j in range(i+i, N, i):
                L[j] = False
    for i in range(M, N):
        if i > 1 and L[i] == True:
            print(i)


solve(N, M)

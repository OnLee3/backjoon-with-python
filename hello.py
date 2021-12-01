import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
Area = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]
DP[0][0] = Area[0][0]


def search(x, y):
    for i in range(1, x):
        DP[0][i] = Area[0][i] + DP[0][i-1]
    for i in range(1, y):
        DP[i][0] = Area[i][0] + DP[i-1][0]
    for i in range(1, y):
        for j in range(1, x):
            DP[i][j] = Area[i][j] + max(DP[i-1][j], DP[i][j-1])
    return DP[y-1][x-1]


print(search(M, N))

import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
List = []

for _ in range(N):
    a, b, c = map(int, input().split())
    List.append([a, b, c])
dp = List

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] += min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] += min(dp[i-1][j-1], dp[i-1][j+1])
        else:
            dp[i][j] += min(dp[i-1][j-2], dp[i-1][j-1])

print(min(dp[N-1]))

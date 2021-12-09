import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
List = [list(map(int, input().split())) for i in range(N)]


def solve(N):
    dp = [[0]*i for i in range(1, N+1)]
    dp[0][0] = List[0][0]
    for i in range(1, N):
        for j in range(i+1):
            dp[i][j] = List[i][j]
            if j == 0:
                dp[i][j] += dp[i-1][0]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[N-1])


print(solve(N))

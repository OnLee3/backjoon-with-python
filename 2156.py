import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
wines = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] * (n+2)
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

# 인접한 포도주를 마신경우, 두번째 전의 포도주를 마신경우, 이번 포도주를 마시지 않을 경우
for i in range(3, n+1):
    dp[i] = max(wines[i-1] + dp[i-3] + wines[i], dp[i-2] + wines[i], dp[i-1])

print(dp[n])

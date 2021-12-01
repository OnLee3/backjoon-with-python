import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
remain = 1000000009


def Sum(N):
    dp = [1, 2, 4]
    if N > 3:
        for _ in range(N-3):
            dp.append((dp[-3] + dp[-2] + dp[-1]) % remain)
    return dp


N = [int(input()) for _ in range(T)]
result = Sum(max(N))

[print(result[n-1])for n in N]


# dp = [0 for _ in range(Max)]
# dp[0] = 1
# dp[1] = 2
# dp[2] = 4


# for i in range(3, Max):
#     dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % remain

# [print(dp[int(input())-1]) for _ in range(T)]

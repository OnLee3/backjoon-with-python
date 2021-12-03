import sys


def input():
    return sys.stdin.readline().rstrip()


def solve(N):
    dp = [0, 1, 2, 3, 5, 8]
    if N > 5:
        for i in range(N-5):
            dp.append((dp[-2] + dp[-1]) % 15746)
    return dp[N]


print(solve(int(input())))

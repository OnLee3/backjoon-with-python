import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())


def solve(N):
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N > 10:
        for i in range(N-10):
            dp.append((dp[-1] + dp[-5]))
    return dp


N = [int(input()) for _ in range(T)]
DP = solve(max(N))
[print(DP[n]) for n in N]

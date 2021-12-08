import sys


def input():
    return sys.stdin.readline().rstrip()


def solve(H):
    dp = [1, 1, 3, 5]
    if H > 3:
        for _ in range(H-3):
            current = 0
            for i in range(len(dp)-1):
                current += dp[i]
            dp.append(current*2+1)
    return dp[H]


H = int(input())
print(solve(H))

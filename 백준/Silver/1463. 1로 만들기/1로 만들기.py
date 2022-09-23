from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


x = int(input())
dp = [-1 for _ in range(1000001)]


def BFS(x):
    Q = deque()
    Q.append(x)
    dp[x] = 0
    while Q:
        x = Q.popleft()
        if x == 1:
            return
        if x % 3 == 0 and dp[x//3] == -1:
            dp[x//3] = dp[x] + 1
            Q.append(x // 3)
        if x % 2 == 0 and dp[x//2] == -1:
            dp[x//2] = dp[x] + 1
            Q.append(x // 2)
        if dp[x-1] == -1:
            dp[x-1] = dp[x] + 1
            Q.append(x - 1)


BFS(x)
print(dp[1])

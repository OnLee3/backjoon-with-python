import sys


def input():
    return sys.stdin.readline().rstrip()


A = list(map(str, input()))
B = list(map(str, input()))
dp = [0] * 1001

for i in range(len(A)):
    cnt = 0
    for j in range(len(B)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif A[i] == B[j]:
            dp[j] = cnt+1
print(max(dp))

import sys

def input():
  return sys.stdin.readline().rstrip()  

n, k = map(int, input().split())
dp=[[0]*(k+1) for _ in range(n+1)]

def solve(n, k):
  if dp[n][k]:
    return dp[n][k]
  if n == k or k == 0:
    dp[n][k] = 1
    return 1
  else:
    dp[n][k] = solve(n-1, k) + solve(n-1, k-1)
    return dp[n][k]
print(solve(n, k))
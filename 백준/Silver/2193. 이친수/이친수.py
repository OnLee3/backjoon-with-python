import sys

def input():
  return sys.stdin.readline().rstrip()

dp=[0, 1, 1, 2, 3, 5]

n = int(input())

for i in range(6, n+1):
  dp.append(dp[-2]+dp[-1])

print(dp[n])
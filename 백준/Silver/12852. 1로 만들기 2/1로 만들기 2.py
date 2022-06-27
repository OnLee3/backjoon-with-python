import sys

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
dp = [[] for _ in range(n+1)]
dp[1].append(1)

for i in range(2, n+1):
  dp[i] = dp[i-1]+[i]
  if i%3 == 0 and len(dp[i]) > len(dp[i//3])+1:
    dp[i] = dp[i//3] + [i]
  if i%2 == 0 and len(dp[i]) > len(dp[i//2])+1:
    dp[i] = dp[i//2] + [i]
answer = list(map(str, reversed(dp[n])))
print(len(answer) - 1)
print(" ".join(answer))
import sys
import math

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
dp = [4] * (n+1)
dp[1] = 1

for i in range(2, n+1):
  if int(math.sqrt(i))**2 == i:
    dp[i] = 1
  else:
    j=1
    while (j**2 < i):
      dp[i] = min(dp[j**2] + dp[i-j**2], dp[i])
      j+=1

print(dp[n])
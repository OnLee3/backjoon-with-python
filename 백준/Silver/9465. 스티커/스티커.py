import sys

def input():
  return sys.stdin.readline().rstrip()  

for _ in range(int(input())):
  n=int(input())
  board=[list(map(int, input().split())) for _ in range(2)]
  dp=[[0]*n for _ in range(2)]
  dp[0][0] = board[0][0]
  dp[1][0] = board[1][0]

  for j in range(1, n):
    for i in range(2):
      if i == 0:
        dp[i][j] = max(dp[i][j-1], dp[i+1][j-1] + board[i][j])
      elif i == 1:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + board[i][j])
  print(max(dp[0][n-1], dp[1][n-1]))
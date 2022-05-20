import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

t = int(input())  

def dfs(graph, start):
  q = deque([start])
  if dp[start] == -1:
    dp[start] = 1
  while q:
    v = q.popleft()
    color = dp[v]
    for i in graph[v]:
      if dp[i] == -1:
        q.append(i)
        dp[i] = 0 if color == 1 else 1
      elif dp[i] == color:
          return False
  return True

for _ in range(t):
  v, e = map(int, input().split())
  graph=[[] for _ in range(v+1)]
  dp=[-1 for _ in range(v+1)]
  for __ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1, v+1):
    if not dfs(graph, i):
      print("NO")
      break
  else:
    print("YES")
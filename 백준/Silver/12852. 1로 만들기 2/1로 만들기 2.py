import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())

def bfs(n):
  q = deque([[n]])
  while q:
    state = q.popleft()
    if (state[-1] == 1):
      return state
    if (state[-1] % 3 == 0):
      cur = state[:]
      cur.append(state[-1]//3)
      q.append(cur)
    if (state[-1] % 2 == 0):
      cur = state[:]
      cur.append(state[-1]//2)
      q.append(cur)
    cur = state[:]
    cur.append(state[-1]-1)
    q.append(cur)
answer = list(map(str, bfs(n)))
print(len(answer)-1)
print(" ".join(answer))
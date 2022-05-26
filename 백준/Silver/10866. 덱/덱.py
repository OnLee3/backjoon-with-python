import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()  
q = deque([])

for _ in range(int(input())):
  s = list(input().split())
  if s[0] == 'push_front':
    q.appendleft(s[1])
  elif s[0] == 'push_back':
    q.append(s[1])
  elif s[0] == 'pop_front':
    if len(q) > 0:
      print(q.popleft())
    else:
      print(-1)
  elif s[0] == 'pop_back':
    if len(q) > 0:
      print(q.pop())
    else:
      print(-1)
  elif s[0] == 'size':
    print(len(q))
  elif s[0] == 'empty':
    if len(q)>0:
      print(0)
    else:
      print(1)
  elif s[0] == 'front':
    if len(q)>0:
      print(q[0])
    else:
      print(-1)
  elif s[0] == 'back':
    if len(q)>0:
      print(q[-1])
    else:
      print(-1)
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()  

for _ in range(int(input())):
  n, m = map(int, input().split())
  l = [[i] for i in range(n)]
  tmp = list(map(int, input().split()))
  for i in range(n):
    l[i].append(tmp[i])
  q=deque(l)
  q2=deque(tmp)
  cnt=0

  while q:
    if max(q2) == q[0][1]:
      cnt+=1
      i, v = q.popleft()
      q2.popleft()
      if i == m:
        print(cnt)
        break
    else:
      i, v = q.popleft()
      v2 = q2.popleft()
      q.append([i, v])
      q2.append(v2)
      
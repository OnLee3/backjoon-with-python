import sys

def input():
  return sys.stdin.readline().rstrip()  

m = int(input())
s = set()

for _ in range(m):
  v = input().split()
  
  if len(v) == 1:
    if v[0] == 'all':
      s = set([i for i in range(1, 21)])
    else:
      s = set()
    continue
    
  order, x = v[0], int(v[1])
  if order == 'add':
    s.add(x)
  elif order == 'check':
    print(1 if x in s else 0)
  elif order == 'remove':
    s.discard(x)
  elif order == 'toggle':
    if x in s:
      s.discard(x)
    else:
      s.add(x)
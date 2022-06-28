import sys

def input():
  return sys.stdin.readline().rstrip()  

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle=0
# 사이클 판별
for i in range(1, e+1):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle=i
        break
    else:
        union_parent(parent, a, b)
print(cycle)
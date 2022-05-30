import sys

def input():
  return sys.stdin.readline().rstrip()  

n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
  v = input()
  dic[str(i)] = v
  dic[v] = i
for _ in range(m):
  v = input()
  print(dic[v])
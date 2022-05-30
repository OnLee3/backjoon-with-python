import sys

def input():
  return sys.stdin.readline().rstrip()  

n, m = map(int, input().split())
s = set([])
answer = []

for _ in range(n):
  v = input()
  s.add(v)

for _ in range(m):
  v = input()
  if v in s:
    answer.append(v)

print(len(answer))
[print(i) for i in sorted(answer)]
    
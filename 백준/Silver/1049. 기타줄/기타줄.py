import sys

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
brands = [list(map(int, input().split())) for _ in range(m)]
answer=0
a = sorted(brands, key=lambda x: x[0])[0][0]
b = sorted(brands, key=lambda x: x[1])[0][1]

while n > 0:
  if n <= 6:
    if b*n < a:
      answer += b*n
      n = 0
    else:
      answer += a
      n -= 6
  else:
    if b*6 < a:
      answer += b*6
      n -= 6
    else:
      answer += a
      n -= 6

print(answer)
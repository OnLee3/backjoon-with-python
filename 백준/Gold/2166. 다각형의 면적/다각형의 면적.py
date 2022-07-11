import sys

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
x = []
y = []
ans = 0

for _ in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)
  
x += [x[0]]
y += [y[0]]

for i in range(n):
  ans += (x[i]*y[i+1])-(x[i+1]*y[i])
  
print(round(abs(ans)/2,1))
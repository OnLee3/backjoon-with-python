import sys

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
s = input()
r = 31
M = 1234567891


answer=0
for i in range(n):
  answer += (ord(s[i])-96) * (r**i)
print(answer%M)
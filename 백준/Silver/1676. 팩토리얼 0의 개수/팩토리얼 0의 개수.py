import sys

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
answer=1
for i in range(1, n+1):
  answer=answer*i
cnt=0
for i in reversed(str(answer)):
  if i != '0':
    break
  cnt+=1
print(cnt)
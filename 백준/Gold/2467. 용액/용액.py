import sys

def input():
  return sys.stdin.readline().rstrip()  

n = int(input())
arr = list(map(int, input().split()))
Max = sys.maxsize
ans = [arr[0], arr[n-1]]

left=0
right=n-1

while left < right:
  res = arr[left] + arr[right]
  if (Max > abs(res)):
    Max = abs(res)
    ans = [arr[left], arr[right]]
  if (res > 0):
    right-=1
  elif (res < 0):
    left+=1
  else:
    break
    
print(ans[0], ans[1])
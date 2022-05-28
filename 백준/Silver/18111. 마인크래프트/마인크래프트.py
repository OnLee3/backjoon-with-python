import sys
from itertools import chain

def input():
  return sys.stdin.readline().rstrip()  
  
n, m, b = map(int, input().split())
board=list(chain.from_iterable([list(map(int, input().split())) for _ in range(n)]))
board.sort(reverse=True)
dp=[]

for i in range(257):
  tmp=0
  block=b
  for j in board:
    gap=abs(i-j)
    if j > i:
      block+=gap
      tmp+=gap*2
    elif j < i:
      if block >= gap:
        block-=gap
        tmp+=gap
      else:
        break
  else:
    dp.append(tmp)

ans_floor = min(dp)
print(ans_floor, [i for i, value in enumerate(dp) if value == ans_floor][-1])
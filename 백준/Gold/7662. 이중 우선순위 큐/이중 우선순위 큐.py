import sys
import heapq

def input():
  return sys.stdin.readline().rstrip()  

for _ in range(int(input())):
  minQ = []
  maxQ = []
  visited = [False] * (int(1e6)+1) 
  for i in range(int(input())):
    tmp = input().split()
    order, x = tmp[0], int(tmp[1])
    if order == 'I':
      heapq.heappush(minQ, (x, i))
      heapq.heappush(maxQ, (-x, i))
      visited[i] = True
    else:
      if x == 1:
        while maxQ and not visited[maxQ[0][1]]: heapq.heappop(maxQ)
        if maxQ:
          visited[maxQ[0][1]] = False
          heapq.heappop(maxQ)
      else:
        while minQ and not visited[minQ[0][1]]: heapq.heappop(minQ)
        if minQ:
          visited[minQ[0][1]] = False
          heapq.heappop(minQ)
  while maxQ and not visited[maxQ[0][1]]:heapq.heappop(maxQ)
  while minQ and not visited[minQ[0][1]]:heapq.heappop(minQ)
  if minQ and maxQ:
    print(-maxQ[0][0], minQ[0][0])
  else:
    print("EMPTY")
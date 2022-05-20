import sys

def input():
  return sys.stdin.readline().rstrip()

left = list(input())
right = []
m = int(input())

for _ in range(m):
  order = list(input().split())
  if (order[0] == 'P'):
    left.append(order[1])
  elif (order[0] == 'L'):
    if left:
      right.append(left.pop())
  elif (order[0] == 'D'):
    if right:
      left.append(right.pop())
  elif (order[0] == 'B'):
    if left:
      left.pop()

left.extend(reversed(right))
print(''.join(left))

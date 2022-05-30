import sys

def input():
  return sys.stdin.readline().rstrip()  

n, m = map(int, input().split())

stack = []

for _ in range(n):
  stack.append(input())

for _ in range(m):
  inp = input()
  try:
    v = int(inp)
    print(stack[v-1])
  except ValueError:
    v = inp
    print(stack.index(v)+1)
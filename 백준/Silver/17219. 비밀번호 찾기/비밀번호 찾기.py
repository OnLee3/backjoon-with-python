import sys

def input():
  return sys.stdin.readline().rstrip()  

table = dict()
n, m = map(int, input().split())

for _ in range(n):
  site, password = input().split()
  table[site] = password
for _ in range(m):
  site = input()
  print(table[site])
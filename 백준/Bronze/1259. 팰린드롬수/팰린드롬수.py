import sys

def input():
  return sys.stdin.readline().rstrip()  

while True:
  n = input()
  if int(n) == 0:
    break
  if n == str(int(''.join(list(reversed(list(n)))))):
    print('yes')
  else:
    print('no')
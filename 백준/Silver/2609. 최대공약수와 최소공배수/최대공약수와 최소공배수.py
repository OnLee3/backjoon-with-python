import sys
import math

def input():
  return sys.stdin.readline().rstrip()

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
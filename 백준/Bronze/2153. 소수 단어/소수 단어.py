import sys
import math

def input():
  return sys.stdin.readline().rstrip()

def is_prime(x):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return "It is not a prime word."
  return "It is a prime word."

s = input()
answer = 0

for letter in s:
  v = ord(letter)
  v -= 96 if v >= 97 else 38
  answer += v 

print(is_prime(answer))
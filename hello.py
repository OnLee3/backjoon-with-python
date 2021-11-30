import sys


def input():
    return sys.stdin.readline().rstrip()


A, B, C = map(int, input().split())
N = int(input())
Max = 0

for _ in range(N):
    Sum = 0
    for __ in range(3):
        a, b, c = map(int, input().split())
        Sum += ((A*a) + (B*b) + (C*c))
    Max = max(Max, Sum)

print(Max)

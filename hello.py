import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
Schedule = [int(input()) for _ in range(N)]
Gap = []

for i in range(N-1):
    Gap.append(Schedule[i+1] - Schedule[i])
if K != 1:
    Gap = sorted(Gap)[:-(K-1)]

print(sum(Gap) + K)

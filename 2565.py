import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
wires = []
dp = [1]*n

for i in range(n):
    a, b = map(int, input().split())
    wires.append((a, b))

wires.sort()
print(wires)

for i in range(n):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))

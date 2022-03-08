import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
numbers = list(map(int, input().split()))

increase = [1]*n
decrease = [1]*n
result = []


for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if numbers[i] > numbers[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(n):
    result.append(increase[i]+decrease[i]-1)

print(max(result))

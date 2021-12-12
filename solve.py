import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
List = list(map(int, input().split()))
List.sort()
answer = 0
current = 0

for x in List:
    current += x
    answer += current
print(answer)

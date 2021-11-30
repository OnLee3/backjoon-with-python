import sys
from operator import itemgetter


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
List = list(map(int, input().split()))
answer = 0
Max = 0
cnt = 0

for i in List:
    if i > Max:
        cnt = 0
        Max = i
    else:
        cnt += 1
    answer = max(cnt, answer)

print(answer)

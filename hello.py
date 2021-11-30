import sys
from operator import itemgetter


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
Schedule = []
et = 0
cnt = 0

for _ in range(N):
    start, end = map(int, input().split())
    Schedule.append([start, end])
Schedule = sorted(Schedule, key=itemgetter(1, 0))

for meeting in Schedule:
    if meeting[0] >= et:
        cnt += 1
        et = meeting[1]
print(cnt)

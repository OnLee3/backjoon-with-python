import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


heap = []


def solve(x):
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))


[solve(int(input())) for _ in range(int(input()))]

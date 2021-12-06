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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)


[solve(int(input())) for _ in range(int(input()))]

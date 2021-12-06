import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


leftHeap = []
rightHeap = []


def solve(x):
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-x, x))
    else:
        heapq.heappush(rightHeap, x)
    if rightHeap and leftHeap[0][1] > rightHeap[0]:
        Min = heapq.heappop(rightHeap)
        Max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-Min, Min))
        heapq.heappush(rightHeap, Max)
    print(leftHeap[0][1])


[solve(int(input())) for _ in range(int(input()))]

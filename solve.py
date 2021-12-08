import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
Prime = list(map(int, input().split()))
heap = []
[heapq.heappush(heap, x) for x in Prime]

for i in range(K):
    current = heapq.heappop(heap)
    for j in range(N):
        heapq.heappush(heap, current * Prime[j])
        if current % Prime[j] == 0:
            break
else:
    print(current)

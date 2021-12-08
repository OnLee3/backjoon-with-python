import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def solve(N):
    if N == 1:
        return 0
    else:
        heap = []
        answer = 0

        for _ in range(N):
            heapq.heappush(heap, int(input()))

        for _ in range(N-1):
            deck1 = heapq.heappop(heap)
            deck2 = heapq.heappop(heap)
            answer += deck1 + deck2
            heapq.heappush(heap, deck1 + deck2)

        return answer


N = int(input())
print(solve(N))

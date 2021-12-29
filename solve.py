import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    cnt = 0
    visited[1] = True
    Queue = deque([1])
    while Queue:
        V = Queue.popleft()
        for i in graph[V]:
            if not visited[i]:
                Queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt


print(bfs())

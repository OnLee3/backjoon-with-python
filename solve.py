import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, M, V = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    visited[v] = True
    Queue = deque([v])
    while Queue:
        v = Queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                Queue.append(i)
                visited[i] = True


dfs(V)
print()
visited = [False] * (N+1)
bfs(V)

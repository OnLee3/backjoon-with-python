import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(M)]
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1


bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer-1)

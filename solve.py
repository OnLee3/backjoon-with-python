import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline().rstrip()


def solve():
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(j, i)
                cnt += 1
    print(cnt)


def dfs(x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
        if x-1 >= 0:
            dfs(x-1, y)
        if x+1 < M:
            dfs(x+1, y)
        if y-1 >= 0:
            dfs(x, y-1)
        if y+1 < N:
            dfs(x, y+1)
    else:
        return


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    solve()

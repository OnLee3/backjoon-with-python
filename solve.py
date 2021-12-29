import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
List = [list(map(int, input())) for _ in range(N)]
answer = []
cnt = 0


def dfs(x, y):
    global cnt
    if List[x][y] == 1:
        List[x][y] = 0
        cnt += 1
        if x+1 < N:
            dfs(x+1, y)
        if x-1 >= 0:
            dfs(x-1, y)
        if y+1 < N:
            dfs(x, y+1)
        if y-1 >= 0:
            dfs(x, y-1)
    return cnt


for i in range(N):
    for j in range(N):
        if List[i][j] == 1:
            cnt = 0
            answer.append(dfs(i, j))

answer.sort()
print(len(answer))
[print(i) for i in answer]

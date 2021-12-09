import sys


def input():
    return sys.stdin.readline().rstrip()


def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
            return False
    return True


def dfs(x):
    global answer
    if x == N:
        answer += 1
        return
    for i in range(N):
        col[x] = i
        if check(x):
            dfs(x+1)


N = int(input())
answer = 0
col = [0]*15

dfs(0)
print(answer)

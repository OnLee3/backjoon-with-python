import sys

N, M = map(int, sys.stdin.readline().split())
L = [sys.stdin.readline().rstrip() for _ in range(N)]
A = []


def makeGame(flag, y, x):
    cnt = 0
    for i in range(8):
        if i > 0:
            if flag == "W":
                flag = "B"
            elif flag == "B":
                flag = "W"
        for j in range(8):
            if flag == "W" and L[y + i][x + j] != "W":
                cnt += 1
            elif flag == "B" and L[y + i][x + j] != "B":
                cnt += 1
            if flag == "W":
                flag = "B"
            elif flag == "B":
                flag = "W"
    return cnt


for y in range(N):
    if y + 8 > N:
        break
    for x in range(M):
        if x + 8 > M:
            break
        A.append(min(makeGame("W", y, x), makeGame("B", y, x)))


print(min(A))

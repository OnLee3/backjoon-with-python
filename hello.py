import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
answer = []


def solve(N, M):
    for i in range(N, M+1):
        if i == 1:
            continue
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            answer.append(i)
    if len(answer) > 0:
        print(sum(answer))
        print(min(answer))
    else:
        print(-1)


solve(N, M)

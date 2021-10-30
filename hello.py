import sys

N = int(sys.stdin.readline())

cnt = 2
answer = 1


def solve(N, cnt, answer):
    if cnt > N:
        return print(answer)
    answer = answer * cnt
    cnt += 1
    solve(N, cnt, answer)


solve(N, cnt, answer)

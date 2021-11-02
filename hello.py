import sys

N = int(sys.stdin.readline())
A = [0, 1]


def solve(A, cnt):
    if cnt > N:
        print(A[N])
    else:
        A.append(A[cnt-2] + A[cnt-1])
        cnt += 1
        solve(A, cnt)


solve(A, 2)

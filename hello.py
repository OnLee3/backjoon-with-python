import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())


def solve(N):
    if N <= 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 4
    if N == 4:
        return 7
    return (solve(N-3) + solve(N-2) + solve(N-1))


[print(solve(int(input()))) for _ in range(T)]

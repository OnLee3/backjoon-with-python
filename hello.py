import sys

a, b, c = map(int, sys.stdin.readline().split())


def solve(k, n):
    if n == 0:
        return 1
    recur = solve(k, n//2) % c
    if n % 2 == 0:
        return recur * recur
    else:
        return recur * recur * k


print(solve(a, b) % c)

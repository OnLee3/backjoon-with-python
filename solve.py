import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
Stack = []


def solve(x):
    if x == 0:
        Stack.pop()
    else:
        Stack.append(x)


[solve(int(input())) for _ in range(N)]
print(sum(Stack))

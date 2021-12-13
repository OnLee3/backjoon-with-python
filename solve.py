import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


def solve(PS):
    Stack = []
    for x in PS:
        if x == "(":
            Stack.append(x)
        else:
            if len(Stack):
                Stack.pop()
            else:
                return "NO"
    if len(Stack):
        return "NO"
    else:
        return "YES"


[print(solve(input())) for _ in range(N)]

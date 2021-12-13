import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
Stack = []


def solve(x):
    if x[0] == 'push':
        Stack.append(int(x[1]))
    elif x[0] == 'pop':
        if len(Stack):
            print(Stack.pop())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(Stack))
    elif x[0] == 'empty':
        if len(Stack):
            print(0)
        else:
            print(1)
    elif x[0] == 'top':
        if len(Stack):
            print(Stack[-1])
        else:
            print(-1)


[solve(list(input().split())) for _ in range(N)]

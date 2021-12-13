import sys


def input():
    return sys.stdin.readline().rstrip()


def solve(S):
    Stack = []
    for x in S:
        if x == "(" or x == "[":
            Stack.append(x)
        elif x == ")":
            if Stack:
                last = Stack.pop()
                if last != "(":
                    return "no"
            else:
                return "no"
        elif x == "]":
            if Stack:
                last = Stack.pop()
                if last != "[":
                    return "no"
            else:
                return "no"
    if Stack:
        return "no"
    else:
        return "yes"


while True:
    S = input()
    if S == ".":
        break
    print(solve(S))

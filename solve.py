import sys


def input():
    return sys.stdin.readline().rstrip()


S = input()
List = []
answer = 0

for i in S:
    if i in List:
        answer += len(List) - List.index(i) - 1
        List.remove(i)
    else:
        List.append(i)
print(answer)

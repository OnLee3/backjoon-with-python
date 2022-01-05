import sys


def input():
    return sys.stdin.readline().rstrip()


C, N = map(int, input().split())
chickens = []
cows = []
answer = 0

[chickens.append(int(input())) for _ in range(C)]
[cows.append(list(map(int, input().split()))) for _ in range(N)]
chickens.sort()
cows.sort(key=lambda x: (x[1], x[0]))

for cow in cows:
    for chicken in chickens:
        if cow[0] <= chicken <= cow[1]:
            answer += 1
            chickens.remove(chicken)
            break
print(answer)

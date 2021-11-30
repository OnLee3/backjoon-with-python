import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
List = [int(input()) for _ in range(N)]
List.reverse()

cnt = 0
for i in List:
    cnt += K // i
    K = K % i
print(cnt)

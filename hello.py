import sys

N = int(sys.stdin.readline().rstrip())
List = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    List.append([b, a])

List = sorted(List)

for i in range(N):
    print(List[i][1], List[i][0])

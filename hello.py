import sys

N = int(sys.stdin.readline())
List = []

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    List.append([int(age), name])

for age, name in sorted(List, key=lambda x: x[0]):
    print(age, name)

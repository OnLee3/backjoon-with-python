import sys

N = int(sys.stdin.readline())
List = [int(sys.stdin.readline()) for _ in range(N)]
List.sort()
[print(i) for i in List]

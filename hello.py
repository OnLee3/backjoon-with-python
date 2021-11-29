import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
List = [i for i in range(1, N+1)]

for i in list(combinations(List, M)):
    print(" ".join(map(str, i)))

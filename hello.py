import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
List = [i for i in range(1, N+1)]

for i in list(combinations_with_replacement(List, M)):
    print(" ".join(map(str, i)))

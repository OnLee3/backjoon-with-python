import sys
import math

A = list(map(int, sys.stdin.readline().split()))


def solve(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)-i):
            if A[j-1] > A[j]:
                [A[j-1], A[j]] = [A[j], A[j-1]]
    print(A)


solve(A)

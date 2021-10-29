import sys
import math

A = list(map(int, sys.stdin.readline().split()))


def solve(A):
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        [A[i], A[minIndex]] = [A[minIndex], A[i]]
    for i in A:
        print(i)


solve(A)

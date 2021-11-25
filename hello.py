import sys

N = int(sys.stdin.readline())
A = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))


def solve(check, array, start, end):
    if start > end:
        return(0)
    mid = (start + end)//2
    if array[mid] == check:
        return(1)
    elif array[mid] > check:
        return solve(check, array, start, mid-1)
    else:
        return solve(check, array, mid+1, end)


s = 0
e = len(A)-1
[print(solve(i, A, s, e)) for i in B]

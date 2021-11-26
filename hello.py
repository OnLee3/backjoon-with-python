import sys

N = list(str(sys.stdin.readline().rstrip()))
N.sort(reverse=True)
print("".join(N))

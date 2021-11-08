import sys

N = int(sys.stdin.readline())
A = []
R = []

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    cnt = 1
    for j in range(N):
        if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
            cnt += 1
    R.append(str(cnt))
print(" ".join(R))

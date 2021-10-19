import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0:
        X = N // H
        Y = H
    else:
        X = 1 + (N // H)
        Y = N % H
    if X < 10:
        X = "0" + str(X)
    answer = str(Y) + str(X)
    print(answer)

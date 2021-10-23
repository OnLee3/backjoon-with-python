import sys
N = int(sys.stdin.readline())

for i in range(2, N+1):
    if i * i > N:
        break
    while N % i == 0:
        print(i)
        N = int(N / i)
if N > 1:
    print(N)

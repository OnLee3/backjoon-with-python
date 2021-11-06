import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
Max = 300000
Answer = 0


def solve(N, M, A, Max, Answer):
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                Sum = A[i]+A[j]+A[k]
                if M-Sum < Max and Sum <= M:
                    Max = M-Sum
                    Answer = Sum
    return Answer


print(solve(N, M, A, Max, Answer))

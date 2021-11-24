import sys

N, K = map(int, sys.stdin.readline().split())
p = 1000000007


def power(n, k):
    if k == 0:
        return 1
    x = power(n, k//2)
    if k % 2 == 0:
        return (x ** 2) % p
    else:
        return (x ** 2 * n) % p


Fact = [1 for _ in range(N+1)]

for i in range(2, N+1):
    Fact[i] = Fact[i-1] * i % p

A = Fact[N]
B = Fact[K] * Fact[N-K] % p

print((A % p) * (power(B, p-2) % p) % p)

import sys


def input():
    return sys.stdin.readline().rstrip()


MAX = 21
dp = [[[0] * MAX for __ in range(MAX)]for _ in range(MAX)]


def solve(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return solve(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = solve(a, b, c-1) + solve(a, b-1, c-1) - solve(a, b-1, c)
    else:
        dp[a][b][c] = solve(a-1, b, c) + solve(a-1, b-1, c) + \
            solve(a-1, b, c-1) - solve(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {solve(a, b, c)}")

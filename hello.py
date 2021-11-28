import sys

T = int(sys.stdin.readline().rstrip())

zero = [1, 0, 1]
one = [0, 1, 1]


def solve(N):
    if len(zero) > N:
        return (str(zero[N]), str(one[N]))
    zero.append(zero[len(zero)-2] + zero[len(zero)-1])
    one.append(one[len(one)-2] + one[len(one)-1])
    return solve(N)


[print(" ".join(solve(int(sys.stdin.readline()))))for _ in range(T)]

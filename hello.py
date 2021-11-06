import sys

N = int(sys.stdin.readline())


def solve(Disk, From, To, Sub):
    if Disk == 1:
        print(From, To)
    else:
        solve(Disk-1, From, Sub, To)
        print(From, To)
        solve(Disk-1, Sub, To, From)


print(2**N-1)
solve(N, 1, 3, 2)

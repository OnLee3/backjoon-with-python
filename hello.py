import sys

N = int(sys.stdin.readline())
List = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]
a = 0
b = 0
c = 0


def solve(x, y, length):
    first = List[y][x]

    for i in range(length):
        for j in range(length):
            if List[y + i][x + j] != first:
                for k in range(3):
                    for m in range(3):
                        solve(x + (length//3*m), y + (length//3*k), length//3)
                return

    global a, b, c
    if first == "-1":
        a += 1
    elif first == "0":
        b += 1
    else:
        c += 1


solve(0, 0, N)
print(a)
print(b)
print(c)

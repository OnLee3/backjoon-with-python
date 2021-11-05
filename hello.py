import sys

N = int(sys.stdin.readline())

stars = [[" " for _ in range(N)] for _ in range(N)]


def solve(size, x, y):
    if size == 1:
        stars[y][x] = "*"
    else:
        next_size = size // 3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    solve(next_size, x + dx * next_size, y + dy * next_size)


solve(N, 0, 0)
for i in stars:
    print("".join(i))

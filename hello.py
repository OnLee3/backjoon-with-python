import sys

N = int(sys.stdin.readline())
List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0


def divide(x, y, length):
    first = List[y][x]

    for i in range(length):
        for j in range(length):
            if List[y+i][x+j] != first:
                divide(x, y, length//2)
                divide(x + length//2, y, length//2)
                divide(x, y + length//2, length//2)
                divide(x + length//2, y + length//2, length//2)
                return
    if first == 0:
        global white
        white += 1
    else:
        global blue
        blue += 1


divide(0, 0, N)

print(white)
print(blue)

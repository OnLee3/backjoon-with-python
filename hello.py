import sys

N = int(sys.stdin.readline())
List = [sys.stdin.readline().rstrip() for _ in range(N)]
answer = ""


def solve(x, y, length):
    global answer
    first = List[y][x]

    for i in range(length):
        for j in range(length):
            if List[y + i][x + j] != first:
                answer += "("
                solve(x, y, length//2)
                solve(x + length//2, y, length//2)
                solve(x, y + length//2, length//2)
                solve(x + length//2, y+length//2, length//2)
                answer += ")"
                return
    answer += first


solve(0, 0, N)
print(answer)

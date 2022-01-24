BoardLegnth = 9
SudokuBoard = [list(map(int, input().split())) for _ in range(BoardLegnth)]
# 풀이해야할 칸들
Zeros = [(i, j) for i in range(BoardLegnth)
         for j in range(BoardLegnth) if SudokuBoard[i][j] == 0]


def getPromising(x, y):  # 들어갈수 있는 숫자들을 구한다.
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(BoardLegnth):  # 행열을 탐색한다.
        if SudokuBoard[x][i] in promising:
            promising.remove(SudokuBoard[x][i])
        if SudokuBoard[i][y] in promising:
            promising.remove(SudokuBoard[i][y])
    innerX = (x // 3) * 3
    innerY = (y // 3) * 3
    for i in range(3):  # 3 X 3 영역을 탐색한다.
        for j in range(3):
            if SudokuBoard[innerX + i][innerY + j] in promising:
                promising.remove(SudokuBoard[innerX + i][innerY + j])
    return promising


def paintCell(zerosIndex):
    if zerosIndex == len(Zeros):  # 해결해야하는 칸들을 전부 탐색했다면, 정답 출력하고 종료
        [print(" ".join(map(str, i))) for i in SudokuBoard]
        exit(0)
    (x, y) = Zeros[zerosIndex]
    promising = getPromising(x, y)
    for num in promising:  # 가능한 숫자들중 하나를 집어넣고 다음 숫자를 탐색한다.
        SudokuBoard[x][y] = num
        paintCell(zerosIndex+1)
        SudokuBoard[x][y] = 0  # 만일 정답이 아니라면 0으로 되돌린다.


# DFS
paintCell(0)

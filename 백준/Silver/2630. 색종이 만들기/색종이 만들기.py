import sys


def input():
  return sys.stdin.readline().rstrip()


N = int(input())
paper = []

for _ in range(N):
  paper.append(list(map(int, input().split())))

# paper 배열 탐색 시작
# 파라미터: (N, x, y)
# 배열 첫번째 상태(paper[x][y])가 N / 2  * N / 2 전체와 일치하는지 비교.
# 만약 전부 같다면, 재귀 종료.
# 배열 첫번째 상태의 색깔을 ++
# 다른게 발견 된다면, 재귀 함수 4개 호출
# (N/2, x, y)
# (N/2, N/2 + x, y)
# (N/2, x, N/2 + y)
# (N/2, N/2 + x, N/2 + y)

blue = 0
white = 0

def recur(n, x, y):
  initState = paper[x][y]
  for i in range(n):
    for j in range(n):
      nx = i + x
      ny = j + y
      if (initState != paper[nx][ny] and n != 1):
        recur(int(n / 2), x, y)
        recur(int(n / 2), int(n / 2) + x, y)
        recur(int(n / 2), x, int(n / 2) + y)
        recur(int(n / 2), int(n / 2) + x, int(n / 2) + y)
        return
  if initState == 1:
    global blue
    blue = blue + 1
  else:
    global white
    white = white + 1

recur(N, 0, 0)

print(white)
print(blue)

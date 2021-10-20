import sys
T = int(sys.stdin.readline())
people = [[0 for j in range(14)] for i in range(15)]
for i in range(15):
    people[i][0] = 1
for j in range(14):
    people[0][j] = j + 1
for i in range(1, 15):
    for j in range(1, 14):
        people[i][j] = people[i][j - 1] + people[i - 1][j]
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(people[k][n-1])

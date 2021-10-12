import sys

N = int(sys.stdin.readline())
cN = N
flag = True
answer = 0

while flag == True:
    ten = (cN % 10) * 10
    one = (int(cN / 10) + cN % 10) % 10
    cN = ten + one
    answer += 1
    if cN == N:
        flag = False
print(answer)

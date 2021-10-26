import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))
    maxN = max(num)
    if maxN == 0:
        break
    num.remove(maxN)

    if ((num[0] ** 2) + (num[1] ** 2)) ** 0.5 == maxN:
        print("right")
    else:
        print("wrong")

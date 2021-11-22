import sys

N = int(sys.stdin.readline())
countArray = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    countArray[num] += 1

for i in range(1, 10001):
    count = countArray[i]
    for _ in range(count):
        print(i)

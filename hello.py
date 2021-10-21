import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in num_list:
    if i == 1:
        continue
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        answer += 1
print(answer)

import sys
N, M, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

biggest = 0
big = 0
answer = 0
for x in num_list:
    if x >= biggest:
        big = biggest
        biggest = x

while M > 0:
    for i in range(1, K+1):
        answer += biggest
        M -= 1
        if M <= 0:
            break
    if M <= 0:
        break
    else:
        answer += big
        M -= 1
print(answer)

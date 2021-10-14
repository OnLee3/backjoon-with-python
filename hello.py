import sys
N = int(sys.stdin.readline())
cnt = 0

for i in range(N):
    S = sys.stdin.readline().rstrip()
    flag = False
    for j in range(len(S)):
        linear = True
        for k in range(j+1, len(S)):
            if S[j] != S[k]:
                linear = False
            elif S[j] == S[k] and k - j > 1 and linear == False:
                flag = True
                break
    if flag == False:
        cnt += 1
print(cnt)

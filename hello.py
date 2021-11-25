import sys
from collections import Counter

N = int(sys.stdin.readline())
A = sorted([int(sys.stdin.readline()) for _ in range(N)])


def Avg():
    return round(sum(A) / N)


def Mid():
    return A[N // 2]


def Mode():
    mode = Counter(A).most_common(2)
    if len(mode) > 1 and mode[0][1] == mode[1][1]:
        return mode[1][0]
    else:
        return mode[0][0]


def Range():
    return max(A) - min(A)


print(Avg())
print(Mid())
print(Mode())
print(Range())

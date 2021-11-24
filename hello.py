import sys

N = int(sys.stdin.readline())
count = [0 for _ in range(10)]


def pageCount(pages, pValue):
    if pages:
        replaced = int(str(pages//10) + "9")
        gap = replaced - pages

        for i in range(len(count)):
            count[i] += (pages//10 + 1) * pValue
        for i in range(10-gap, 10):
            count[i] -= pValue
        for i in list(str(pages)[:-1]):
            count[int(i)] -= gap * pValue

        count[0] -= pValue
        pageCount(pages//10, pValue*10)


pageCount(N, 1)
print(" ".join(map(str, count)))

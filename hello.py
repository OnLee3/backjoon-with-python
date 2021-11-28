import sys

N = int(sys.stdin.readline())
List = list(set(sys.stdin.readline().rstrip() for _ in range(N)))
sortedList = []

for i in List:
    sortedList.append((len(i), i))

for length, word in sorted(sortedList):
    print(word)

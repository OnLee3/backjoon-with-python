import sys

N = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
sortedList = sorted(set(List))
dictList = {}
answer = []

for i in range(len(sortedList)):
    dictList[sortedList[i]] = i

for i in List:
    answer.append(str(dictList[i]))

print(" ".join(answer))

import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


def isValid(perm):
    vowelCount = 0
    consonantCount = 0
    for letter in perm:
        if letter in vowel:
            vowelCount += 1
        else:
            consonantCount += 1
    if consonantCount < 2 or vowelCount < 1:
        return False
    return True


vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
List = sorted(list(input().split()))
perm = list(combinations(List, L))
result = list(filter(isValid, perm))

[print("".join(i)) for i in result]

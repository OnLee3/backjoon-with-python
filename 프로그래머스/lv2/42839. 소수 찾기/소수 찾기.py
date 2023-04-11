from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    unique_numbers = set()
    answer=0
    
    for length in range(1, len(numbers)+1):
        for perm in permutations(numbers, length):
            number = int("".join(perm))
            if is_prime(number):
                unique_numbers.add(number)
    return len(unique_numbers)
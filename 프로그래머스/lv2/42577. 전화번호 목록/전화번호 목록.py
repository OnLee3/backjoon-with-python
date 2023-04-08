def solution(phone_book):
    prefix_map = {}

    for number in phone_book:
        for i in range(len(number)):
            prefix = number[:i+1]
            if prefix in prefix_map:
                prefix_map[prefix] += 1
            else:
                prefix_map[prefix] = 1

    for number in phone_book:
        if prefix_map[number] > 1:
            return False

    return True

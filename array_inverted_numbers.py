def solution(numbers):
    # TODO: implement solution here
    result = []
    n = len(numbers)
    for i in range(n):
        str_numbers = str(numbers[i])
        inverted = int(str_numbers[::-1])
        if inverted in numbers:
            result.append((numbers[i], inverted))
        else:
            None
    return result
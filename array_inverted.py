from math import sqrt

def solution(numbers):
    # TODO: implement this function
    result = []
    n = len(numbers)
    for i in range(n):
        result.append((numbers[i], (round(sqrt(numbers[n-i-1]*numbers[i]),2)))))
    return result
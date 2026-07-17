def array_with_conditional_interruption(inputString, numbers):
    sum_so_far = 0
    i = 0
    while i < len(inputString) and sum_so_far < 20:
        result += 'a' if inputString[i] == 'z' else chr(ord(inputString[i]) + 1)
        half_number = round(numbers[i] / 2)
        sum_so_far += half_number
        i += 1
    return result[::-1], numbers[i:]
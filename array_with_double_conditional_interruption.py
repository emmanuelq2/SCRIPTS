def array_with_double_conditional_interruption(inputString, numbers):
    sum_temp = 0
    i = 0
    result = ''
    while i < len(inputString) and inputString[i] not in vowels and sum_temp < 100:
        result += 'z' if inputString[i] == 'a' else chr(ord(inputString[i]) - 1)
        half_number = abs(numbers[i] * 2)
        sum_temp += half_number
        i += 1
    return result, numbers[i:]
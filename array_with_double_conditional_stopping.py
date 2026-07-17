def array_with_double_conditional_stopping(inputString, numbers):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    sum_temp = 0
    i = 0
    result = ''
    vowels = 'aeiou'
    while i < len(inputString) and sum_temp < 100 and i < len(numbers):
        result += vowels[(vowels.index(inputString[i]) + 1) % len(vowels)] if inputString[i] in vowels else consonants[(consonants.index(inputString[i]) + 1) % len(consonants)]
        half_number = round(numbers[i] * 3)
        sum_temp += half_number
        i += 1
    return result, numbers[i:]


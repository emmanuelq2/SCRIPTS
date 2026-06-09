
import re

def numbers_extraction_sum(s):
    result_tokens = []
    numbers = re.findall(r'\d+', s)
    return sum(int(num) for num in numbers)


'''
def numbers_extraction_sum(text: str) -> int:
    result_tokens = []

    for token in text.split():
        token = token.strip(",.")
        if token.isdigit():
            number = int(token)
            print(number)
            result_tokens.append(number)
                                
    return sum(result_tokens)
'''

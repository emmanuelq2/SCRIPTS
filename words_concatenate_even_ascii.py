
def words_concatenate_even(sentence, c):
    # TODO:  create a Python function that identifies and concatenates the second half of each word with an even  
    # number of characters, ensuring the characters of this second half go before the character c in the ASCII table.
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 0:  # check if the length of word is even
            second_half = word[len(word)//2:]
            for ch in second_half:
                if ord(ch) < ord(c):  # check if character goes before 'c' in ASCII table
                    result += ch
    return result

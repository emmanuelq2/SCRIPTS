def words_characters_odd(sentence):
    # TODO: write a Python function that selects the even-indexed characters of words containing an odd number of characters.
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) % 2 == 1:  # check if the length of word is odd
            for i in range(0, len(word), 2):  # loop over even-indexed characters
                result += word[i]
    return ''.join(reversed(result))
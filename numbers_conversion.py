def swap_letter_number_tokens(text):
    """Swap hyphen-separated tokens between letters and numbers (1..26).

    Rules:
    - a..z  -> 1..26
    - 1..26 -> a..z
    - any other token is kept unchanged
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result_tokens = []

    for token in text.split("-"):
        if len(token) == 1 and token.isalpha() and token.islower():
            result_tokens.append(str(alphabet.index(token) + 1))
        elif token.isdigit():
            number = int(token)
            if 1 <= number <= 26:
                result_tokens.append(alphabet[number - 1])
            else:
                result_tokens.append(token)
        else:
            result_tokens.append(token)

    return "-".join(result_tokens)


if __name__ == "__main__":
    sample = "a-1-z-26-12-b"
    print(swap_letter_number_tokens(sample))
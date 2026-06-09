
def numbers_in_words_moved(s):
    """Move the first letter after each number to just before that number.

    Example:
    "I have 2 apples" -> "I have a2pples"

    The rules for this exercise are:
    - read the text from left to right
    - when a number is found, capture the whole number, not just one digit
    - then look ahead for the first alphabetic character after that number
    - any spaces or punctuation between the number and that letter are removed
    - place that letter immediately before the number
    """

    # This list stores the transformed characters and pieces of text.
    # We build the answer piece by piece, then join everything at the end.
    result = []

    # This variable is our current position while scanning the string.
    # It moves from left to right until we reach the end of the text.
    index = 0

    # Keep processing characters until the entire string has been scanned.
    while index < len(s):
        # If the current character is not a digit, it does not start a number.
        # In that case, copy it as-is into the result.
        if not s[index].isdigit():
            result.append(s[index])

            # Move to the next character and continue scanning.
            index += 1
            continue

        # If we reach this point, we have found the start of a number.
        # Save the starting position so we can slice the whole number later.
        number_start = index

        # Advance index while characters are digits so multi-digit numbers
        # like 12, 345, or 2024 are captured as one full number.
        while index < len(s) and s[index].isdigit():
            index += 1

        # Extract the full number from the original string.
        # Example: if the text contains "12 apples", number becomes "12".
        number = s[number_start:index]

        # Now search for the first alphabetic character that appears
        # after the number. This may skip over spaces and punctuation.
        # Example: in "5! oranges", this loop skips "! " and stops at "o".
        next_letter_index = index
        while next_letter_index < len(s) and not s[next_letter_index].isalpha():
            next_letter_index += 1

        # If we found a letter, move it before the number.
        if next_letter_index < len(s):
            # Add the found letter first.
            result.append(s[next_letter_index])

            # Then add the whole number immediately after that letter.
            result.append(number)

            # Jump to the character after the moved letter.
            # This automatically removes everything between the number and
            # that letter, because those skipped characters are never copied.
            index = next_letter_index + 1
        else:
            # Safety case: if there is no letter after the number,
            # keep the number unchanged.
            result.append(number)

            # At this point, index is already at the end of the number.
            # The outer loop will continue from there.

    # Join all collected pieces into one final string.
    return ''.join(result)


print(numbers_in_words_moved("I have 2 apples and 5! oranges and 3 grapefruits."))
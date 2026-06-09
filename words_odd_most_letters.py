def words_odd_most_letters(sentence):
    words = sentence.split()
    # Store one selected character per odd-length word.
    result = []

    for word in words:
        if len(word) % 2 == 1:
            # Compare letters case-insensitively.
            lower_word = word.lower()
            # Frequency map: character -> number of occurrences in the word.
            counts = {}

            for ch in lower_word:
                # Read one character from the current word.
                # Basic counting without dict.get:
                # if character already exists, increment it; otherwise start at 1.
                if ch in counts:
                    counts[ch] += 1
                else:
                    counts[ch] = 1

            # Pick the most frequent character.
            # Tie-breaker: if counts are equal, keep the earliest character in the word.
            # With minus sign, earlier position becomes a bigger number in the sorting key, so it will be chosen first.
            best_char = max(counts, key=lambda ch: (counts[ch], -lower_word.index(ch)))
            # Add selected character for this odd-length word.
            result.append(best_char)

    # Concatenate all selected characters into the final string.
    return "".join(result)

sentence = "Hello world this is a demo string"
print(words_odd_most_letters(sentence))

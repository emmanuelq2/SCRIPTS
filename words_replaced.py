def replace_inverse_words(sentences, words):
    result = []  # Final list of processed sentences.

    for i, sentence in enumerate(sentences):  # Traverse sentences with their index.
        if i >= len(words):  # If no matching word exists at this index, keep sentence unchanged.
            result.append(sentence)  # Store the original sentence as-is.
            continue  # Move to the next sentence.

        word = words[i]  # Word that corresponds to this sentence (same index).
        rev_word = word[::-1]  # Reverse the matching word.
        capitalized_word = word[:1].upper() + word[1:]  # Capitalized form of the original word.
        capitalized_rev = rev_word[:1].upper() + rev_word[1:]  # Capitalized form of reversed word.

        new_sent = sentence.replace(word, rev_word)  # Replace lowercase occurrences.
        new_sent = new_sent.replace(capitalized_word, capitalized_rev)  # Replace capitalized occurrences.
        result.append(new_sent)  # Save transformed sentence.

    return result  # Return processed sentences.

"""     for sentence in sentences:
        for word in words:
            reversed_words = [w[::-1] for w in words]
            for word_inv in reversed_words:
                actual_sent = sentence.replace(word, word_inv)
                result.append(actual_sent)
            return result """

""" sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e']
words = ['simple', 'bond', 'e']
print(replace_inverse_words(sentences, words)) """
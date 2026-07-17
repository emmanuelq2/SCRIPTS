def sorting_tuples(s):
    if not s:
        return []

    # Accept both strings and lists of characters.
    current = list(s)
    removed_chars = []

    # Repeatedly process consecutive pairs until one character remains.
    while len(current) > 1:
        next_round = []
        for i in range(0, len(current), 2):
            pair = current[i:i + 2]
            if len(pair) == 2:
                a, b = pair
                if a <= b:
                    removed_chars.append(a)
                    next_round.append(b)
                else:
                    removed_chars.append(b)
                    next_round.append(a)
            else:
                next_round.append(pair[0])
        current = next_round

    return removed_chars + current
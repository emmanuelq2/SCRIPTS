def spot_swaps(source: str, target: str) -> list:
    if len(source) != len(target):
        return []

    result = []
    i = 0

    while i < len(source) - 1:
        is_adjacent_swap = (
            source[i] != target[i]
            and source[i + 1] == target[i]
            and source[i] == target[i + 1]
        )

        if is_adjacent_swap:
            result.append((i, source[i], target[i]))
            # "Characters can be swapped at most once” means those two characters must not be reused.
            i += 2
            continue

        i += 1   # Move to the next character if no swap is detected. Otherwise, infinite looping on the same characters.

    return result

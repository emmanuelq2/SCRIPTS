def identifying_pairs_numbers(listA, listB):
    result = []
    seen = set()  # keep only unique pairs, not every repeated occurrence.

    for n1 in listA:
        for n2 in listB:
            if n1 > n2 and (n1, n2) not in seen:
                # store pairs in a set first, or check if the pair is already in the result list before appending.
                seen.add((n1, n2))
                result.append((n1, n2))

    return result

""" listA = [5, 1, 8, -2, 0]
listB = [3, 2, 7, 10, -1]
print(identifying_pairs_numbers(listA, listB)) """
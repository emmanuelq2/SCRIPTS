def array_hopping_stop(arrayA, arrayB):
    if len(arrayA) != len(arrayB):
        raise ValueError("arrayA and arrayB must have the same length")

    indexA = 0
    visitedA = []
    result = []

    while indexA not in visitedA:
        visitedA.append(indexA)

        indexB = arrayA[indexA] - 1   # convert A value (1-based) to 0-based
        result.append(indexB + 1)     # convert back to 1-based for output

        indexA = arrayB[indexB] - 1   # next A index, again converted to 0-based

    return result
def array_hopping(arrayA, arrayB):
    indexA = 0
    indexB = None
    in_arrayA = True
    max_value = float('-inf')
    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            if arrayB[indexB] > max_value:
                max_value = arrayB[indexB]
        else:
            indexA = arrayB[indexB]
            if indexA == 0:
                return max_value
        in_arrayA = not in_arrayA
def array_hopping_stop_conditions(arrayA, arrayB, arrayC):
    """Run 0-based A->B->A->C->A traversal and return maxB + maxC.

    maxB is the maximum encountered value of arrayB[indexB].
    maxC is the maximum encountered value of arrayC[indexC].
    The run stops when an A-position repeats or any hop becomes out of bounds.
    """
    if len(arrayA) != len(arrayB) or len(arrayA) != len(arrayC):
        raise ValueError("arrayA, arrayB and arrayC must have the same length")

    n = len(arrayA)
    if n == 0:
        return None

    indexA = 0
    visitedA = set()
    #  float("-inf") creates a value smaller than every normal number.
    max_b_value = float("-inf")
    max_c_value = float("-inf")

    while True:
        if indexA < 0 or indexA >= n:
            # If we never reached a valid B or C hop, there is no computable result.
            if max_b_value == float("-inf") or max_c_value == float("-inf"):
                return None
            return max_b_value + max_c_value

        if indexA in visitedA:
            if max_b_value == float("-inf") or max_c_value == float("-inf"):
                return None
            return max_b_value + max_c_value
        visitedA.add(indexA)

        # Hop 1: A -> B
        indexB = arrayA[indexA]
        if indexB < 0 or indexB >= n:
            if max_b_value == float("-inf") or max_c_value == float("-inf"):
                return None
            return max_b_value + max_c_value

        # Hop 2: B -> A
        nextA = arrayB[indexB]
        max_b_value = max(max_b_value, arrayB[indexB])
        if nextA < 0 or nextA >= n:
            if max_b_value == float("-inf") or max_c_value == float("-inf"):
                return None
            return max_b_value + max_c_value

        # Hop 3: A -> C (from the A reached through B)
        indexC = arrayA[nextA]
        if indexC < 0 or indexC >= n:
            if max_b_value == float("-inf") or max_c_value == float("-inf"):
                return None
            return max_b_value + max_c_value

        # Hop 4: C -> A
        returntoA = arrayC[indexC]
        max_c_value = max(max_c_value, arrayC[indexC])
        indexA = returntoA


"""
Walkthrough:

1. Start indexA = 0
2. Hop A -> B: indexB = arrayA[0] = 1
3. Hop B -> A: nextA = arrayB[1] = 1, so max_b_value becomes 1
4. Hop A -> C: indexC = arrayA[1] = 0
5. Hop C -> A: returntoA = arrayC[0] = 1, so max_c_value becomes 1, indexA = 1
6. Next loop, indexA = 1 is new, continue

7. Hop A -> B: indexB = arrayA[1] = 0
8. Hop B -> A: nextA = arrayB[0] = 2, max_b_value becomes max(1, 2) = 2
9. Hop A -> C: indexC = arrayA[2] = 2
10. Hop C -> A: returntoA = arrayC[2] = 2, max_c_value becomes max(1, 2) = 2, indexA = 2
11. Next loop, indexA = 2 is new, continue

12. Hop A -> B: indexB = arrayA[2] = 2
13. Hop B -> A: nextA = arrayB[2] = 0
14. Hop A -> C: indexC = arrayA[0] = 1
15. Hop C -> A: returntoA = arrayC[1] = 0, indexA = 0
16. Now indexA = 0 was already visited, so it breaks at the repeat condition and returns max_b_value + max_c_value = 2 + 2 = 4

"""
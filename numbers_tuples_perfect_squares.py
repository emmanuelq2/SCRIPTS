def adding_numbers_perfect_square(arr1, arr2):

    # no floating-point rounding issues
    # result is already an integer
    # safer for exact perfect-square checks
    from math import isqrt

    if not arr1 or not arr2:
        return []

    result = []
    for num1 in arr1:
        for num2 in arr2:
            total = num1 + num2
            if total < 0:
                continue

            root = isqrt(total)
            if root * root == total:
                result.append((num1, num2))
    return result

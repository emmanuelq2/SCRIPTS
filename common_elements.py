def common_elements(listA, listB):
    # TODO: Implement the function to find the common elements in the two arrays
    result = []
    for i in listA:
        for j in listB:
            if i == j:
                result.append((i))
    return result

listA = [7, 2, 3, 9, 1] 
listB = [2, 3, 7, 6]
print(common_elements(listA, listB))    

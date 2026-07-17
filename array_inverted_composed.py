""" You are given an array of n integers, where n ranges from 2 to 200, inclusive. 
The elements in the array range from -200 to 200, inclusive. Your task is to return 
an array in which each element is the sum of a pair composed  of an element and its 
'opposite' element. """

def solution(numbers):
    result = []
    left = 0
    right = len(numbers) - 1
    
    # Loop until the pointers cross over each other
    while left <= right:
        if left == right:
            # Odd length middle element pairs with itself
            result.append(numbers[left] + numbers[right])
        else:
            # Pair the opposite elements
            result.append(numbers[left] + numbers[right])
            
        # Move pointers closer together
        left += 1
        right -= 1
        
    return result
# even_numbers_list_comprehension.py
# List comprehension to filter even numbers from a list
numbers = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

# List comprehension to filter positive numbers from a range
numbers = range(-10, 10)
positive_numbers = [i for i in numbers if i >= 0]
print(positive_numbers)

# List comprehension to double numbers in a range
numbers = range(5)
double_numbers = [i * 2 for i in numbers]
print(double_numbers)

# List comprehension to invert numbers in a range
numbers = range(10)
inverted_numbers = [i if i % 2 == 0 else -i for i in numbers]
print(inverted_numbers)

# List comprehension to retrieve even numbers from a range
numbers = range(51)
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)
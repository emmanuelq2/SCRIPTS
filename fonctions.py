liste = [5,3,9,7,1,4,2,6]   
liste = liste.sort()
print(liste) # None

liste = [5,3,9,7,1,4,2,6]   
sorted_list = sorted(liste)
print(sorted_list) # [1, 2, 3, 4, 5, 6, 7, 9]
liste.append(14)
print(liste) # [1, 2, 3, 4, 5, 6, 7, 9, 14]  

book = "lord of the rings"
print(book.title()) # Lord Of The Rings
print(book.capitalize()) # Lord of the rings    
print(book.upper()) # LORD OF THE RINGS
print(book.lower()) # lord of the rings


title = "lord of the rings".title()
print(title) # Lord Of The Rings


# Python built-in functions

# len() method
print(len("Python")) # 6


# round() method
print(round(2.2)) # 2
print(round(2.5)) # 2
print(round(2.6)) # 3

# min & max methods
print(min(1, 2, 3, 4, 5)) # 1
print(max(1, 2, 3, 4, 5)) # 5
print(min("a", "b", "c")) # a
print(max("a", "b", "c")) # c

# sum() methods
print(sum([1, 2, 3, 4, 5])) # 15

# range() method:
print(range(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(10, 1, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(10, 1, -2))) # [10, 8, 6, 4, 2]

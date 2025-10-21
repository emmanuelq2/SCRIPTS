
# for loop
for i in [0,1,4,7,8,6,9,10,11,12]:
    print(i)

for letter in "Python":
    print(letter)

for i in range(10): # print 10 times the string "Bonjour!"
    print("Bonjour!")


# while loop
i = 0
while i < 100:
    print("Bonjour!")
    i += 1

# continuer = 'o'
# while continuer == 'o':
#     print("On continue")
#     continuer = input("Voulez-vous continuer ? (o/n) ")
#     if continuer != 'o':
#         print("Au revoir !")

# import time
# while True:
#     print("Sauvegarde en cours")
#     time.sleep(60) # wait 1 second
 
print(list(range(10)))

liste = []
while liste == True:
    print("Itération sur la liste")

# continue
liste = ["1","2","3","4","Paul","7","Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element) # print the element that is not a digit

# break
liste = ["1","2","3","4","Paul","7","Pierre"]
for element in liste:
    if element.isdigit():
        break # break at the first iteration
    print(element) 

# for - else loop
names = ["Jack", "John", "Peter"]
for name in names:
    if name == "Peter":
        print("Pierre est dans la liste")
        break   
    else:
        print("J'ai trouvé " + name)
    
# list comprehension
liste = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
positive_numbers = [i for i in liste if i > 0]
print(positive_numbers) # print the list of positive numbers
positive_numbers_doubled = [i * 2 for i in liste if i > 0]
print(positive_numbers_doubled) # print the list of positive numbers multiplied by 2

# any & all
import os
print(any([True, False, False, False, True])) # returns True if at least one element is True
print(any([False, False, False, False, False])) # returns False if all elements are False
print(all([True, False, False, False, True])) # returns False if at least one element is False
# all([f.endswith(".jpg") for f in os.listdir("images")]) # returns True if all elements end with ".jpg"
print(all([f.endswith(".jpg") for f in os.listdir("images")])) # returns True if all elements end with ".jpg"


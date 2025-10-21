# lists

liste = [1,2,2,3,4,5,6,7,8,9,10]
print(liste)
liste2 = [250,"Python",True]

## lists methods
# append method
liste.append(11)
liste.append(12)
liste.append(14)
print(liste)
liste.append([10,14,16])

# remove method
liste.remove(2)
liste.remove(2)
print(liste)
print(liste)
print(liste[0])
print(liste[-1])
print(liste[-1][1]) # 14

liste3 = ["Java", "Python", "C++"]
liste3.remove("Python")
liste3.append("Python")
# liste3[1] = "C++"
# liste3[2] = "Python"
print(liste3)

liste_nb = [3, 8, 5, 2, 1, 4, 6, 7, 9]
liste_nb.remove(2) # remove the first occurrence of 2']
liste_nb.remove(4)
liste_nb.remove(3)
print(liste_nb) # [8, 5, 1, 6, 7, 9]

# slicing method
liste4 = ["Utilisateur_1", "Utilisateur_2", "RUtilisateur_3", "Utilisateur_4", 
          "Utilisateur_5", "Utilisateur_6", "Utilisateur_7", "Utilisateur_8",
          "Utilisateur_9", "Utilisateur_10"]
print(liste4[1:2])
print(liste4[0:2])
print(liste4[:])
print(liste4[2:]) # all elements from index 2 to the end
print(liste4[:-1]) # all elements except the last one
print(liste4[::2]) # every odd elements starting from index 0 to the last one
print(liste4[1::2]) # every even elements starting from index 1 to the last one
print(liste4[3::2]) # every even elements starting from index 4 to the last one


# index method
employees = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

print(employees.index("Carlos")) # returns the index of the first occurrence of "Carlos"
print(employees.index("Alex")) # returns the index of the first occurrence of "Alex"

# count method
employees = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Carlos", "Carlos"]  
print(employees.count("Carlos")) # returns the number of occurrences of "Carlos"
resultat = employees.count("Carlos")
print(resultat) # returns the number of occurrences of "Carlos"

# sort the list
employees = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employees.sort()
print(employees)

sorted_list = sorted(employees) # sorted() returns a new list
print(sorted_list)

# reverse the list
employees = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employees.reverse() # reverse the list
print(employees)

employees.sort(reverse=True) # sort in reverse order
print(employees)

# pop() method
element = employees.pop(-1)
print(element) # remove the last element and return it
print(employees) # print the list after removing the last element  = "Alex"

# clear() method
employees.clear() # remove all elements from the list
print(employees) # print the list after removing all elements

# join() method
liste = ["python", "est", "un", "langage", "de", "programmation"]
resultat = " ".join(liste)
print(resultat)
resultat = "_".join(liste)
print(resultat)
resultat = "\n".join(liste)
print(resultat)
resultat = "\t".join(liste)
print(resultat)

# split() method
courses = "Riz, Pâtes, Lait, Viande, Légumes, Fruits"
courses = courses.split() # split the string into a list of strings ['Riz,', 'Pâtes,', 'Lait,', 'Viande,', 'Légumes,', 'Fruits']
print(courses) # print the list of strings
courses = "Riz, Pâtes, Lait, Viande, Légumes, Fruits"
courses_list = courses.split(",") # ['Riz', ' Pâtes', ' Lait', ' Viande', ' Légumes', ' Fruits']
print(courses_list)
courses_list = courses.split(", ") 
print(courses_list) # ['Riz', 'Pâtes', 'Lait', 'Viande', 'Légumes', 'Fruits']


# in, not in
# in operator
users = ["Paul", "Peter", "Mary", "John"]
if "Paul" in users:
    users.remove("Paul")
    print(users) # remove "Paul" from the list


liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]
print(liste[0]) # "Python"
print(liste[1]) # ["Java", "C++", ["C"]]
print(liste[1][0]) # "Java"
print(liste[1][1]) # "C++"
print(liste[0][0:2]) # "Py"

# tuple
tuple_name = (1, 2, 3)
tuple_name2 = (250,"Python",True)
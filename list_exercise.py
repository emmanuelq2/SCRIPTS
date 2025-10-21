liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
first_three = liste[:3]
print(first_three)
last_three = liste[-3:]
print(last_three)
middle = liste[1:-1]
print(middle)
first_last = (liste[0], liste[-1])
print(first_last)
first_last2 = liste[::len(liste)-1]
print(first_last2)

liste = [1, 2, 3, 4, 5]
liste.append(6)
print(liste)
if 6 in liste:
    print("Le nombre 6 a bien été ajouté à la liste.")

langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]
print(python)
deux = nombres[1][1][0]
print(deux)
# sept = nombres[4][0][0]
sept = nombres[-1][0][0]
print(sept)
# variable declaration
first = second = ""

# looping on input until both are digits
while not (first.isdigit() and second.isdigit()):
    first = input("Donne un premier nombre : ")
    second = input("Donne un second nombre : ")

# Solution 1
    if not (first.isdigit() and second.isdigit()):
        print("Veuillez entrer deux nombres valides")

addition = int(first) + int(second)
print("Le resultat de l'addition de ", first, " avec ", second, "est égal à ", addition)

# Solution 2
# print(f"Le resultat de l'addition de {premier} avec {second} est égal à {addition}")
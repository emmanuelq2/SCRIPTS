# lower, upper, capitalize, title methods
print("Bonjour".lower())
print("Bonjour".upper())
print("Bonjour".capitalize())   # capitalizes the first letter of the string and lowercases the rest
print("Bonjour".title())


# replace method
print("bonjour".replace("jour", "soir"))
print("bonjour bonjour".replace("jour", "soir"))
print("bonjour bonjour".replace(" ", ""))
print("bonjour bonjour".replace(" ", "").replace("jour", "soir"))

# strip method
print("bonjour".strip())
print("bon jour".strip())
print(" bonjour ".strip())
print(" bon jour ".strip(" ujor"))
print(" bon jour ".rstrip(" ujor"))
print(" bon jour ".lstrip(" ujor"))

# split & join methods
print("1, 2, 3, 4, 5".split(", "))  # output a list: ['1', '2', '3', '4', '5']
print(", ".join("1 ,2, 3, 4, 5".split(", ")))
print(".".join("1, 2, 3, 4, 5".split(", "))) # providing a character at the start of the string
print(",".join(["1", "2", "3", "4", "5"]))

# zfill method()
print("9".zfill(4))
for i in range(100):
    print(str(i).zfill(4))

# is methods
print("bonjour".islower()) # True
print("Bonjour".islower()) # False
print("Bonjour".istitle()) # True
print("Bonjour tout le monde".istitle())    # True
print("Bonjour tout le monde".isdigit())    # False
print("50".isdigit())   # True
print("50.0".isdigit()) # False     # False, because of the dot
print("50a".isdigit())  # False     # False, because of the letter

# count method
print("bonjour jour".count("jour"))
print("bonjour jour".count(" jour")) # 1 space before "jour" to find a word within a chain of character
print("bonjour".count("o"))
print("bonjour".count("o", 0, 5))
print("bonjour".count("o", 0, 4))

# find & index methods
print("Bonjour le jour".find("jour"))
print("Bonjour le jour".index("jour"))

print("Bonjour le jour".find("soir")) # returns -1 if not found
# print("Bonjour le jour".index("soir")) # raises an exception if not found
# print("Bonjour le jour".index("jour", 0, 5)) # raises an exception if not found
print("Bonjour le jour".find("jour", 0, 5)) # returns -1 if not found
print("Bonjour le jour".find("jour", 5, 10)) # returns -1 if not found  
# print("Bonjour le jour".index("soir")) # raises an exception if not found
# rfind method
print("Bonjour le jour".rfind("jour"))

# endswith & startswith methods
print("Bonjour le jour".endswith("jour")) # True
print("Bonjour le jour".endswith("jour", 0, 5)) # False
print("Bonjour le jour".endswith("jour", 5, 10)) # True
print("Bonjour le jour".startswith("Bonjour")) # True
print("Bonjour le jour".startswith("Bonjour", 0, 5)) # True
print("Bonjour le jour".startswith("Bonjour", 5, 10)) # False
print("image.png")
print("image.png".endswith(".png")) # True
print("image.png".endswith(".jpg")) # False
print("image.png".startswith(".jpg"))   # False         
print("image.png".startswith(".jpg"))    # False      
print("image.png".startswith("image"))    # True
print("image.png".startswith("video"))      # False  

# exercise 1
letter = "o"
phrase = "Bonjour tout le monde"

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum."""
     
result = lorem.count(".")
print(result)

# sort alphabetically a string of names
chaine = "Pierre, Julien, Anne, Marie, Lucien"

# method 1
chaine_en_ordre = chaine.split(", ")
# print(chaine_en_ordre)
chaine_en_ordre = sorted(chaine_en_ordre)
# print(chaine_en_ordre)
print(", ".join(chaine_en_ordre)) # 2

# method 2
chaine_liste = chaine.split(", ")
chaine_liste.sort()
print(", ".join(chaine_liste)) # 3

# method 3
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre) # 4

# method 4
chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(", ")
liste_en_ordre = sorted(chaine_liste)
chaine_en_ordre = ", ".join(liste_en_ordre)
print(chaine_en_ordre) # 5
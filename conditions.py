
# if else
# # first exercise
age = 20
if age >= 18:
    print("Vous êtes majeur !")
else:
    print("Vous êtes mineur !")

# second exercise
language = "Python"
if language == "Python":
    print("You're learning Python! Congrats!")

# elif
age = 17
if age >= 18:
    print("Vous êtes majeur !")
elif age < 18:
    print("Vous êtes mineur !")

# else
user = "admin"
if user == "admin":
    print("Access authorized")
else:
    print("Access denied")

user = "Paul"
if user == "admin":
    print("Access authorized")
elif user == "root":
    print("Access authorized")
else:
    print("Access denied")

# and, or, not

# Ne modifie pas les lignes suivantes
import sys
note = int(sys.argv[-1])
commentaire = ""

""" try:
   note = int(sys.argv[-1])
except ValueError:
   print("Stupid user, please enter a number")
   sys.exit(1) """
     
if note < 3 :
    commentaire = "Sans commentaire..."
elif note >= 18 and note < 20:
    commentaire = "Excellent !!"
elif note == 20:
    commentaire = "C'est un sans faute !"
elif note > 14 :
    commentaire = "Bon travail !"
elif note > 10 :
    commentaire = "Peut mieux faire."
elif note > 6 :
    commentaire = "Il faut tout revoir..."
elif note >= 3:
    commentaire = "Tu n'as rien compris !"
     
print(commentaire)
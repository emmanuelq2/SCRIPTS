prenom = "Paul"
print(f"Bonjour {prenom} !")

a = 5
b = 10
print(f"La multiplication de {a} et {b} est {a * b}")


age = 26
phrase = f"J'ai {age} ans".format(age)
print(f"J'ai {age} ans".format(age))
phrase = f"J'ai {a} ans".format(a=age) # a is defined as 5, but we want to use age
print(f"J'ai {a} ans".format(a=age))

print(f"J'ai {age} ans, {age} ce n'est pas très âgé".format(age=50))


print(f"J'ai {0} ans, {0} ce n'est pas très âgé".format(age))
# print(f"J'ai {} ans, {} ce n'est pas très âgé".format(prenom,age)) # SyntaxError: unexpected character after line continuation character
# print(f"J'ai {0} ans, {0} ce n'est pas très âgé".format(age)) # J'ai 0 ans, 0 ce n'est pas très âgé
print(f"J'ai {age} ans, je m'appelle {prenom}".format(prenom,age)) # J'ai 1 ans, 0 ce n'est pas très âgé
# print(f"J'ai {1} ans, {0} ce n'est pas très âgé".format(prenom,age)) # J'ai 1 ans, 0 ce n'est pas très âgé

protocole = "http:"
nom_du_site = "Docstrings"
extension = "fr"

# Methode 1: Avec l'opérateur +
url = protocole + "//www." + nom_du_site + "." + extension
print(url)

# Methode 2: Avec la méthode format()
url = "{}//www.{}.{}".format(protocole, nom_du_site, extension)
print(url)
url = "{protocole}//www.{domaine}.{extension}".format(protocole=protocole, domaine=nom_du_site, extension='fr')
print(url)

# Methode 3: Avec la méthode f-string
url = f"{protocole}//www.{nom_du_site}.{extension}"
print(url)
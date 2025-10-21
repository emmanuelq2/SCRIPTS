# mdp = input("Entrez votre mot de passe : ")
# if len(mdp) < 8:
#     print("VOTRE MOT DE PASSE DOIT CONTENIR AU MOINS 8 CARACTERES")
# else:
#     if mdp.isdigit == True:
#         print("Votre mot de passe ne contient que des nombres.")
#     else:
#         print("Votre mot de passe est valide.")

# mdp = input("Entrez votre mot de passe : ")
# if mdp.isdigit == True:
#     print("Votre mot de passe ne contient que des nombres.")
# elif len(mdp) < 8:
#     print("VOTRE MOT DE PASSE DOIT CONTENIR AU MOINS 8 CARACTERES")
# elif len(mdp) > 8 and mdp.isdigit == False:
#     print("Votre mot de passe est valide.")

mdp = input("Entrez votre mot de passe : ")
if len(mdp) < 8:
    print("VOTRE MOT DE PASSE DOIT CONTENIR AU MOINS 8 CARACTERES")
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")
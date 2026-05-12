# Les fonctions en python
# Définir une fonction
def dire_bonjour(prénom):
    message = "Bonjour, " + prénom + " !"
    return message
#Appeler la fonction
resultat = dire_bonjour("Jopie")
print(resultat)
# Fonction avec calcul
def calculer_age(année_naissance):
    age = 2026 - année_naissance
    return age

mon_age = calculer_age(1976)
print("Ton âge approximatif est :", mon_age, "ans")

# Fonction avec condition
def evaluér_niveau(nb_competences):
    if nb_competences >= 5:
        return "🏆 Niveau Expert !"
    elif nb_competences >= 3:
        return "🌱 Niveau Intermédiaire "
    else:
        return "🌱 Niveau Débutant"
niveau = evaluér_niveau(5)
print("Ton niveau est :", niveau)
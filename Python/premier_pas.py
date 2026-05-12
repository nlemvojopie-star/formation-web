print("Bonjour")
# print = afficher,"Bonjour" = le texte
print("Bonjour, je m'appelle Jopie !")   
# les variables
prenom = "Jopie"
age = 50
est_developpeur = True
print("prenom:", prenom)
print("je suis développeur:", est_developpeur)
# Une opération mathématique
année_naissance = 2026 - age
print("année de naissance approximative:", année_naissance)
# Les listes
competences = ["HTML", "CSS", "JavaScript", "Git", "Python"]
print("Mes compétences :", competences)
print("Nombre de compétences :", len(competences))

print("--- Mes compétences une par une ---")
for competence in competences:
    print("✓", competence)

if len(competences) >= 5:
    print("🎉 Tu es un développeur complet !")
else:
    print("Continue d'apprendre !")
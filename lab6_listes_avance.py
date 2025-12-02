notes = [12, 9, 15, 8, 17, 13, 19, 10]


# ETAPE 1
if not notes:
    print("Aucune note à traiter.")
    exit()

total = 0
nb_notes = len(notes)

for note in notes:
    total += note

moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")

#ETAPE 2 
notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes après bonus :", notes_bonus)

#ETAPE 3 
seuil = 12
notes_valides = [note for note in notes if note >= seuil]
print(f"Notes ≥ {seuil} : {notes_valides}")

#ETAPE 4 
# Calculer les moyennes
moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / nb_notes  

# Construire le rapport
lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")  
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append("Détails par étudiant :")

# Ajouter les détails par étudiant
for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    lignes.append(f"  Étudiant {index:02d} -- note {note:>5.2f} -> bonus {bonus:>5.2f}")

# Fusionner et afficher
rapport = "\n".join(lignes)
print(rapport)

# (Optionnel) Sauvegarder dans un fichier
with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)
print("\n→ Rapport sauvegardé dans 'rapport_notes.txt'")

#ETAPE 5 

# Test 1: Normaliser sur 100 points
print("\n1. Normalisation sur 100 points :")
notes_sur_100 = [note * 5 for note in notes]  
print(f"Notes sur 100 : {notes_sur_100}")

# Test 2: Catégoriser les étudiants
print("\n2. Catégorisation des étudiants :")
categories = []
for note in notes:
    if note >= 12:
        categories.append("Validé")
    elif note >= 10:
        categories.append("Rattrapage")
    else:
        categories.append("Non Validé")
print(f"Catégories : {categories}")

# Compter chaque catégorie
print(f"  Validés : {categories.count('Validé')} étudiants")
print(f"  Rattrapage : {categories.count('Rattrapage')} étudiants")
print(f"  non validé: {categories.count('Non Validé')} étudiants")

# Test 3: Top 3 des notes
print("\n3. Top 3 des meilleures notes :")
top3 = sorted(notes, reverse=True)[:3]
print(f"Top 3 : {top3}")
print(f"Moyenne du top 3 : {sum(top3)/len(top3):.2f}")
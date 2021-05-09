#Stylo a 5€
#Je recherche le tarif TTC
#Le taux de TVA est a 20%

article="stylo"
print(type(article))
prix=5
taux=0.2
montant_tva=prix*taux
montant_ttc=prix+montant_tva
print("designation      montant montant ttc")
print(article,"         ",montant_tva,"     ",montant_ttc)
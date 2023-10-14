n1 = float(input("Entrez le premier nombre : "))

n2 = float(input("Entrez le deuxième nombre : "))

if n1 == 0 or n2 == 0:
    print("Le produit est nul.")
elif (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
    print("Le produit est positif.")
else:
    print("Le produit est négatif.")

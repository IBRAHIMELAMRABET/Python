L1 = input("Entrez la premier liste d'entiers séparés par des espaces : ").split()
L1 = [int(x) for x in L1]
L2 = input("Entrez la deuxieme liste d'entiers séparés par des espaces : ").split()
L2 = [int(x) for x in L2]
L3 = []
for nb in L1:
    if nb in L2 and nb not in L3:
        L3.append(nb)

print("Intersection des listes L1 et L2 : ", L3)

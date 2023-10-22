L = input("Entrez une liste d'entiers séparés par des espaces : ").split()
L = [int(x) for x in L]
nb = int(input("Entrez le nombre à supprimer : "))

while nb in L:
    L.remove(nb)
print("Liste après suppression :", L)
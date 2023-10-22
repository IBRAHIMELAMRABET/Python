L = input("Entrez une liste d'entiers séparés par des espaces : ").split()
L = [int(x) for x in L]
nb = int(input("Entrez le nombre à rechercher : "))
indices = []
occurrences = 0

for i, number in enumerate(L):
    if number == nb:
        indices.append(i)
        occurrences += 1

if occurrences > 0:
    print(f"Le nombre {nb} a été trouvé {occurrences} fois aux indices : {indices}")
else:
    print(f"Le nombre {nb} n'a pas été trouvé dans la liste.")
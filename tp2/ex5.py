
L = [1, 3, 5, 7, 9]
val = float(input("Entrez un nombre : "))
i = 0
while i < len(L) and L[i] < val:
    i += 1
L.insert(i, val)

print(L)

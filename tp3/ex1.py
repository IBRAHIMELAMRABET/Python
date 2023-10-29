def somme(m, n):
    total = 0
    for i in range(m, n + 1):
        total += i
    return total

resultat = somme(5, 8)
print("La somme est :", resultat)

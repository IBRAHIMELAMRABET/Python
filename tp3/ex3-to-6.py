def conversion_temps(h, m, s):
    return (h * 3600) + (m * 60) + (s)


def conversion_distance(km, m, cm):
    return (km * 1000) + m + (cm / 100)


def vitesse(h, minu, s, km, m, cm):
    distance = conversion_distance(km, m, cm)
    temps = conversion_temps(h, minu, s)
    return distance / temps


def temps_ecoule(heure1, minute1, seconde1, heure2, minute2, seconde2):
    temps1 = conversion_temps(heure1, minute1, seconde1)
    temps2 = conversion_temps(heure2, minute2, seconde2)

    duree = abs(temps2 - temps1)
    return duree


h1 = 8
m1 = 30
s1 = 15

h2 = 12
m2 = 45
s2 = 50

print(f"Le nomber des seconds dans cette horaire est : {conversion_temps(h1, m1, s1)}")
temp = temps_ecoule(h1, m1, s1, h2, m2, s2)
print("Temps écoulé entre les deux horaires en secondes :", temp)

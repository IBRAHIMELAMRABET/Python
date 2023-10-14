temps = float(input("Entrez le temps en minutes : "))

distance = float(input("Entrez la distance en kilomètres : "))

vitesse=(distance*1000)/(temps*60)

print(f"La vitesse est de {vitesse:.2f} mètres par seconde")

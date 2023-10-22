import random

print("On va jouer a un petit jeu, je vais générer un nombre entre 1 et 100 et tu vas le devinez en 7 essais :\n")

num = random.randint(1, 100)
find = False
for i in range(7):
    x = int(input())
    if x == num:
        print(f"Bravo {num} est le nombre que j 'ai choisit")
        print(f"Vous 1'avez deviné {i + 1} essais")
        find = True
        break
    elif 0 < x < num and i != 7:
        print("Oups, entrez un nombre plus grand !")
    elif num < x < 100 and i != 7:
        print("Oups, entrez un nombre plus petit !")
    elif i != 7:
        print("Oups ,vous avez saisi un nombre en dehors de 1 ' intervalle")

if not find:
    print(f"J'ai gagné, je suis le meilleur,\n Le nombre que j 'ai deviné est {num}\n Au revoir !")

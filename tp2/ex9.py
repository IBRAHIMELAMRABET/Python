def euro_to_mad(euro):
    return euro * 10.8


def mad_to_euro(mad):
    return mad * 0.092


conversion = int(input("Choisissez la direction de conversion (euro en MAD (0) ou MAD en euro (1) : "))
values = []
if conversion == 0:
    print("Conversion de l'euro en dirham marocain (MAD).")
    while True:
        value = float(input("Saisissez une valeur en euro (saisie négative pour arrêter) : "))
        if value < 0:
            break
        values.append(euro_to_mad(value))
elif conversion == 1:
    print("Conversion du dirham marocain (MAD) en euro.")
    while True:
        value = float(input("Saisissez une valeur en dirham (saisie négative pour arrêter) : "))
        if value < 0:
            break
        values.append(mad_to_euro(value))
else:
    print("Direction de conversion non reconnue. Veuillez choisir 'euro en MAD' ou 'MAD en euro'.")

if values:
    print("Valeurs converties :")

    for value in values:
        if conversion == 1:
            print(f"{value}  Euro")
        else :
            print(f"{value}  MAD")
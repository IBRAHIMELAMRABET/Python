def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def NombreRacine(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0


def AfficheNombreRacine(a, b, c):
    nb = NombreRacine(a, b, c)
    print(f"La fonction admit {nb} solutions")


def Racine1(a, b, c):
    D = delta(a, b, c)
    x1 = (-b + D ** 0.5) / (2 * a)
    return x1
def Racine2(a, b, c):
    D = delta(a, b, c)
    x1 = (-b - D ** 0.5) / (2 * a)
    return x1

a = 1
b = -6
c = 8

AfficheNombreRacine(a, b, c)

if NombreRacine(a, b, c) == 2:
    print("Racine 1 :", Racine1(a, b, c))
    print("Racine 2 :", Racine2(a, b, c))
elif NombreRacine(a, b, c) == 1:
    print("Racine :", Racine1(a, b, c))

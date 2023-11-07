class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y


class Rectangle(Point):
    def __init__(self, x=0, y=0, longueur=0, largeur=0):
        super().__init__(x, y)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def __str__(self):
        return f"Rectangle de longueur {self.longueur}, de largeur {self.largeur} en {super().__str__()}"


    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, x=0, y=0, longueur=0, largeur=0, hauteur=0):
        super().__init__(x, y, longueur, largeur)
        self.hauteur = hauteur

    def aire(self):
        return 2 * (self.longueur * self.largeur + self.largeur * self.hauteur + self.longueur * self.hauteur)

    def volume(self):
        return self.longueur * self.largeur * self.hauteur

    def __str__(self):
        return f"Parallelepipede de longueur {self.longueur}, de largeur {self.largeur}, de hauteur {self.hauteur} en {super().__str__()}"


    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur



p = Point(3, 4)
print(p)

r = Rectangle(0, 0, 5, 3)
print(r)
print("Aire du rectangle :", r.aire())

par = Parallelepipede(0, 0, 5, 3, 2)
print(par)
print("Aire du parallelepipede :", par.aire())
print("Volume du parallelepipede :", par.volume())

class Batiment:
    def __init__(self, adresse=""):
        self.adresse = adresse

    def __str__(self):
        return f"Adresse : {self.adresse}"

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse


class Maison(Batiment):
    def __init__(self, adresse="",nbPieces=0):
        super().__init__(adresse)
        self.nbPieces=nbPieces
    def get_nbPieces(self):
        return self.nbPieces

    def set_nbPieces(self, nbPieces):
        self.nbPieces = nbPieces

    def __str__(self):
        return f"Maison à l'adresse {self.adresse} avec {self.nbPieces} pièces"

class Immeuble(Batiment):
    def __init__(self,adresse,nbAppart):
        super().__init__(adresse)
        self.nbAppart=nbAppart
    def get_nbAppart(self):
        return self.nbAppart

    def set_nbAppart(self, nbAppart):
        self.nbAppart = nbAppart


    def __str__(self):
        return f"Immeuble à l'adresse {self.adresse} avec {self.nbAppart} appartements"


batiment = Batiment("13 Lot EL Fillaha Errachidia")
print(batiment)
maison = Maison("23 Ain Lati Errachidia", 6)
print(maison)
immeuble = Immeuble("15 Targa Errachidia", 20)
print(immeuble)
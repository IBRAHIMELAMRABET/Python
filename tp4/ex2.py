class Batiment:
    def __init__(self, adresse=""):
        self.adresse = adresse

    def __str__(self):
        return f"Adresse : {self.adresse}"

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse
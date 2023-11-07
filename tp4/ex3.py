class Employe:
    def __init__(self,nom="",prenom=""):
        self.nom=nom
        self.prenom=prenom
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom

    def set_nom(self,nom):
        self.nom=nom
    def set_prenom(self,prenom):
        self.prenom=prenom
    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def gains(self):
        pass

class Patron(Employe):
    def __init__(self,nom="",prenom="",salaire=0):
        super().__init__(nom,prenom)
        self.salaire=salaire

    def get_salaire(self):
        return self.salaire

    def set_salaire(self,salaire):
        self.salaire=salaire

    def __str__(self):
        return f"Patron : {super().__str__()}"
    def gains(self):
        return self.salaire

class TravailleurCommission(Employe):
    def __init__(self,nom="",prenom="",salaire=0,commission=0,quantite=0):
        super().__init__(nom,prenom)
        self.salaire=salaire
        self.commission=commission
        self.quantite=quantite

    def get_salaire(self):
        return self.salaire

    def set_salaire(self, salaire):
        self.salaire = salaire

    def get_commission(self):
        return self.commission

    def set_commission(self,commission):
        self.commission=commission

    def get_quantite(self):
        return self.quantite

    def set_quantite(self,quantite):
        self.quantite=quantite

    def __str__(self):
        return f"Travailleur à commission : {super().__str__()}"

    def gains(self):
        return self.salaire + (self.commission * self.quantite)

class TravailleurHoraire(Employe):
    def __init__(self, nom="", prenom="", retribution=0, heures=0):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures

    def get_heures(self):
        return self.heures
    def get_retribution(self):
        return self.retribution

    def set_heures(self,heures):
        self.heures=heures
    def set_retribution(self,heures):
        self.retribution=heures

    def __str__(self):
        return f"Travailleur horaire : {super().__str__()}"

    def gains(self):
        return self.retribution*self.heures

patron = Patron("Lamrabet", "Ibrahime", 5000)
trav_commission = TravailleurCommission("Slimani", "Ali", 2000, 10, 100)
trav_horaire = TravailleurHoraire("Wastani", "Amal", 20, 160)

print(patron)
print(patron.gains())

print(trav_commission)
print(trav_commission.gains())

print(trav_horaire)
print(trav_horaire.gains())